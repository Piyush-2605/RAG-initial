# RAG PDF Chatbot

A beginner-friendly Retrieval-Augmented Generation (RAG) project using LangChain, FAISS, and Hugging Face embeddings.

---

# Features

* PDF document loading
* Text chunking
* Hugging Face embeddings
* FAISS vector database
* Semantic similarity search
* Modular project structure

---

# Project Structure

```bash
RAG/
│
├── app.py
│
├── data/
│   └── ml_book.pdf
│
├── src/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   └── retriever.py
│
├── requirements.txt
└── README.md
```

---

# Technologies Used

* Python
* LangChain
* FAISS
* Hugging Face Embeddings
* Sentence Transformers

---

# Installation

## Clone the Repository

```bash
git clone <your-repo-url>
cd RAG
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install langchain
pip install langchain-community
pip install langchain-huggingface
pip install langchain-text-splitters
pip install sentence-transformers
pip install faiss-cpu
pip install pypdf
```

---

# Add Your PDF

Place your PDF file inside the `data` folder.

Example:

```bash
data/ml_book.pdf
```

---

# Run the Project

```bash
python app.py
```

---

# Workflow

```text
PDF
 ↓
Document Loader
 ↓
Text Chunking
 ↓
Embeddings
 ↓
FAISS Vector Store
 ↓
Semantic Retrieval
```

---

# Example Query

```python
query = "What is machine learning?"
```

---

# Example Output

```text
Result 1:
Machine learning is a field of artificial intelligence...

Result 2:
Supervised learning is a type of machine learning...
```

---

# Future Improvements

* Add LLM integration
* Build chatbot interface
* Add conversational memory
* Add Streamlit frontend
* Store vector database locally
* Add reranking
* Deploy to cloud

---

# Learning Outcomes

This project helps understand:

* RAG architecture
* Vector embeddings
* Semantic search
* Chunking strategies
* Vector databases
* Modular AI systems

---

# References

* LangChain Documentation
* FAISS Documentation
* Hugging Face
* Sentence Transformers
