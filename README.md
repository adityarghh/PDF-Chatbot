# 📚 PDF Q&A Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.1+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**An intelligent document analysis system powered by Large Language Models**

[Live Demo](#) · [Report Bug](https://github.com/adityarghh/PDF-Chatbot/issues) · [Request Feature](https://github.com/adityarghh/PDF-Chatbot/issues)

</div>

---

## 🎯 Overview

PDF Q&A Chatbot is a production-style Retrieval-Augmented Generation (RAG) application that enables natural language interactions with PDF documents. Built with a focus on modularity and scalability, this system demonstrates practical implementation of vector embeddings, semantic search, and LLM orchestration.

### Key Highlights

- **Intelligent Document Processing**: Automatic text extraction with context-aware chunking
- **Semantic Search**: FAISS-powered vector similarity search for precise information retrieval
- **Conversational AI**: Natural language Q&A grounded strictly in document content
- **Production Architecture**: Modular design with separation of concerns and error handling
- **User-Friendly Interface**: Clean, responsive Streamlit UI with real-time feedback

---

## 🏗️ Architecture

```
┌─────────────────┐
│   PDF Upload    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Text Extraction │
│   & Chunking    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Embedding     │◄──── OpenAI API
│   Generation    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  FAISS Vector   │
│     Store       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  User Query     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Similarity    │
│     Search      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  LLM Response   │◄──── OpenAI GPT
│   Generation    │
└─────────────────┘
```

---

## ✨ Features

### Core Functionality
- **📄 PDF Processing**: Robust text extraction with support for various PDF formats
- **🔍 Semantic Search**: Context-aware retrieval using vector embeddings
- **💬 Conversational Q&A**: Natural language interaction with document content
- **🎯 Source Grounding**: Answers strictly based on uploaded document content
- **⚡ Real-time Processing**: Fast response generation with optimized chunking

### Technical Features
- **Modular Architecture**: Clean separation of UI and business logic
- **Vector Database**: Efficient FAISS indexing for scalable search
- **Error Handling**: Comprehensive exception management and user feedback
- **Environment Configuration**: Secure API key management with `.env` support
- **Responsive UI**: Mobile-friendly Streamlit interface

---

## 🛠️ Technology Stack

| Category | Technology |
|----------|-----------|
| **Language** | Python 3.8+ |
| **Framework** | Streamlit |
| **LLM Orchestration** | LangChain |
| **Vector Store** | FAISS | 
| **Embeddings** | OpenAI `text-embedding-ada-002` |
| **LLM** | OpenAI GPT-3.5/4 |                            (The application can also be adapted to use local models (e.g., Ollama) to avoid API usage)
| **PDF Processing** | PyPDF2 / pdfplumber |

---

## 📁 Project Structure

```
PDF-Chatbot/
│
├── app.py                 # Main Streamlit application
├── helper.py              # Core processing logic
│   ├── PDF loading
│   ├── Text chunking
│   ├── Vector store creation
│   └── Query handling
│
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key with available quota
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/adityarghh/PDF-Chatbot.git
   cd PDF-Chatbot
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Access the application**
   
   Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

---

## 💡 Usage

### Basic Workflow

1. **Upload a PDF**: Click the upload button and select your PDF document
2. **Wait for Processing**: The system will extract text, create embeddings, and build the vector store
3. **Ask Questions**: Type your question in natural language
4. **Get Answers**: Receive contextual answers grounded in your document

### Example Questions

For a research paper:
- "What are the main findings of this study?"
- "Summarize the methodology section"
- "What datasets were used in this research?"

For a business document:
- "What are the key financial metrics mentioned?"
- "Summarize the executive summary"
- "What are the main recommendations?"

---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

### Customization Options

**Chunk Size**: Adjust text chunk size in `helper.py`
```python
chunk_size = 1000  # Default: 1000 characters
chunk_overlap = 200  # Default: 200 characters
```

**Model Selection**: Change the LLM model
```python
model_name = "gpt-3.5-turbo"  # or "gpt-4"
```

**Temperature**: Adjust response creativity
```python
temperature = 0.0  # Range: 0.0 (deterministic) to 1.0 (creative)
```

---

## 🧪 How It Works

### 1. Document Processing
- PDF is uploaded and text content is extracted
- Text is split into overlapping chunks for context preservation
- Each chunk maintains semantic coherence

### 2. Embedding Generation
- Text chunks are converted to vector embeddings using OpenAI's embedding model
- Embeddings capture semantic meaning in high-dimensional space

### 3. Vector Store Creation
- FAISS index is created from embeddings
- Enables fast approximate nearest neighbor search

### 4. Query Processing
- User query is converted to an embedding
- Similarity search retrieves most relevant chunks
- Retrieved context is passed to the LLM

### 5. Response Generation
- LLM generates answer based on retrieved context
- Response is grounded strictly in document content
- Prevents hallucination by constraining to source material

---

## 📊 Performance Considerations

- **Chunk Size**: Smaller chunks provide precise answers; larger chunks give more context
- **Overlap**: Prevents loss of information at chunk boundaries
- **Top-K Retrieval**: Adjusting the number of retrieved chunks affects answer quality
- **Model Selection**: GPT-4 provides better reasoning but costs more than GPT-3.5

---

## 🔮 Future Enhancements

### Planned Features
- [ ] **Multi-PDF Support**: Query across multiple documents simultaneously
- [ ] **Conversation Memory**: Maintain context across multiple questions
- [ ] **Source Citation**: Highlight exact passages used in answers
- [ ] **Local Model Support**: Integration with Ollama/LM Studio for privacy
- [ ] **Export Functionality**: Save Q&A sessions as reports
- [ ] **Advanced Filters**: Filter by document sections or metadata
- [ ] **Multilingual Support**: Process documents in multiple languages

### Technical Improvements
- [ ] Implement caching for repeated queries
- [ ] Add unit tests and integration tests
- [ ] Docker containerization for easy deployment
- [ ] CI/CD pipeline with GitHub Actions
- [ ] Performance monitoring and logging
- [ ] Database integration for session persistence

---

## 🐛 Known Limitations

- Requires active OpenAI API key and internet connection
- API usage incurs costs based on OpenAI pricing
- Performance depends on PDF text extraction quality
- Limited to text-based PDFs (no OCR for scanned documents)
- Single document processing at a time

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Aditya Raj**

- GitHub: [@adityarghh](https://github.com/adityarghh)
- LinkedIn: [@Aditya Raj](www.linkedin.com/in/aditya-raj-79a53b314)

---

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for providing powerful LLM APIs
- [LangChain](https://www.langchain.com/) for the excellent orchestration framework
- [Streamlit](https://streamlit.io/) for the intuitive UI framework
- [FAISS](https://github.com/facebookresearch/faiss) by Facebook Research for efficient similarity search

---

## 📚 Resources

### Documentation
- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Reference](https://platform.openai.com/docs/)

### Learning Resources
- [RAG Systems Explained](https://www.pinecone.io/learn/retrieval-augmented-generation/)
- [Vector Embeddings Guide](https://www.deeplearning.ai/short-courses/google-cloud-vertex-ai/)
- [Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)

---

## 📈 Project Status

**Current Version**: 1.0.0  
**Status**: Active Development  
**Last Updated**: February 2026

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

Made with ❤️ by [Aditya Raj](https://github.com/adityarghh)

</div>


