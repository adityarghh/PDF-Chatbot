import os
import streamlit as st
from dotenv import load_dotenv

st.set_page_config(page_title="DocuQuery")

st.write("App is running ...")


from langchain_openai import ChatOpenAI
from helper import load_pdf, split_text, create_vectorstore

load_dotenv()


st.title("📄 DocuQuery")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Reading and indexing PDF..."):
        text = load_pdf("temp.pdf")
        chunks = split_text(text)
        vectorstore = create_vectorstore(chunks)

    question = st.text_input("Ask a question from the PDF")

    if question:
        llm = ChatOpenAI(
            temperature=0,
            api_key=os.getenv("OPENAI_API_KEY")
        )

        
        docs = vectorstore.similarity_search(question, k=4)
        context = "\n\n".join(doc.page_content for doc in docs)

        prompt = f"""
You are answering questions based ONLY on the context below.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

        answer = llm.invoke(prompt)

        st.markdown("### Answer")
        st.write(answer.content)
