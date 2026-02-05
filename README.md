# PDF Q&A Chatbot

A local PDF question-answering chatbot built using **Streamlit** and **LangChain**.

## Features
- Upload any PDF
- Ask questions based on the document content
- Uses embeddings + vector search (FAISS)
- Simple Streamlit UI

## Tech Stack
- Python
- Streamlit
- LangChain
- FAISS
- OpenAI API

## Setup
```bash
git clone https://github.com/adityarghh/PDF-Chatbot.git
cd PDF-Chatbot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
