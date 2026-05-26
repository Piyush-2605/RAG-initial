# RAG PDF Chatbot

A beginner-friendly Retrieval-Augmented Generation (RAG) project built using LangChain, FAISS, and Hugging Face embeddings.

This project loads PDF documents, converts them into embeddings, stores them in a vector database, and retrieves relevant chunks using semantic similarity search.

---

# Features

* PDF document loading
* Recursive text chunking
* Hugging Face embeddings
* FAISS vector database
* Semantic similarity search
* Modular architecture
* Beginner-friendly RAG pipeline

---

# Project Structure

```bash
RAG/
│
├── .env/
├── data/
├── notebooks/
├── src/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   └── retriever.py
│
├── vectorstore/
├── app.py
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
pip install -r requirements.txt
```

Or manually install:

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

Place your PDF inside the `data` folder.

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
* Add reranking
* Add metadata filtering
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
