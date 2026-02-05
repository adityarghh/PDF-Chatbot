

---

```md
# 📄 PDF Q&A Chatbot

A PDF-based question answering chatbot that allows users to upload a document and ask natural-language questions about its content.  
Built as a local-first prototype using modern LLM tooling and a clean Streamlit interface.

---

## 🚀 Overview

This project demonstrates an end-to-end LLM-powered application workflow:
- Parsing and processing PDF documents
- Converting document text into vector embeddings
- Performing semantic search using a vector database
- Answering user queries grounded strictly in the uploaded document

The focus of this project is clarity, modularity, and practical understanding of how retrieval-augmented generation (RAG) systems work.

---

## ✨ Features

- Upload any PDF file
- Automatic text extraction and chunking
- Vector similarity search using FAISS
- Natural-language question answering
- Clean and minimal Streamlit UI
- Modular, readable codebase

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — UI and app framework
- **LangChain** — document processing and orchestration
- **FAISS** — vector similarity search
- **OpenAI API** — embeddings and chat model

---

## 📁 Project Structure

```

PDF-Chatbot/
├── app.py              # Streamlit app and UI logic
├── helper.py           # PDF loading, chunking, vector store creation
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── .gitignore
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/adityarghh/PDF-Chatbot.git
cd PDF-Chatbot
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

> ⚠️ An active OpenAI API key with available quota is required.

### 5. Run the application

```bash
streamlit run app.py
```

Open your browser at:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. User uploads a PDF file
2. PDF text is extracted and split into manageable chunks
3. Each chunk is converted into vector embeddings
4. FAISS stores embeddings for fast similarity search
5. User queries retrieve the most relevant chunks
6. The language model generates answers grounded in retrieved content

---

## 📌 Notes

* Designed as a local-first prototype
* API usage depends on OpenAI account quota
* Code prioritizes clarity over over-optimization

---

## 🔮 Possible Improvements

* Switch to fully local models (Ollama / LM Studio)
* Support multiple PDFs at once
* Add conversational memory
* Deploy publicly (Streamlit Cloud / Render)
* Highlight source passages used in answers

---

## 👤 Author

Built by **Aditya Raj** as a hands-on LLM application and portfolio project.

```


