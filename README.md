RAG PDF Chatbot

A beginner-to-intermediate Retrieval-Augmented Generation (RAG) project built using LangChain, FAISS, and Hugging Face embeddings.

This project:

Loads PDF documents
Splits text into chunks
Creates embeddings
Stores vectors in FAISS
Retrieves relevant chunks using semantic similarity search
Features
PDF document loading
Recursive text chunking
Hugging Face embeddings
FAISS vector database
Semantic search retrieval
Modular project structure
Project Structure
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
Technologies Used
Python
LangChain
FAISS
all-MiniLM-L6-v2
Hugging Face Embeddings
Installation
1. Clone the Repository
git clone <your-repo-url>
cd RAG
2. Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt

OR manually install:

pip install langchain
pip install langchain-community
pip install langchain-huggingface
pip install langchain-text-splitters
pip install sentence-transformers
pip install faiss-cpu
pip install pypdf
Add Your PDF

Place your PDF inside the data/ folder.

Example:

data/ml_book.pdf
Run the Project
python app.py
Example Workflow
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
Example Query
query = "What is machine learning?"

The retriever searches semantically similar chunks from the PDF.

Example Output
Result 1:
Machine learning is a field of artificial intelligence...

Result 2:
Supervised learning is a type of machine learning...
Core Files
loader.py

Loads PDF documents using PyPDFLoader.

splitter.py

Splits documents into smaller overlapping chunks.

embeddings.py

Creates Hugging Face embedding model.

vectorstore.py

Creates FAISS vector database.

retriever.py

Performs semantic similarity search.

Future Improvements
Add OpenAI/Groq LLM integration
Build conversational memory
Add Streamlit frontend
Store vector DB locally
Add hybrid search
Add reranking
Add metadata filtering
Deploy using Docker or cloud platforms
Learning Outcomes

This project helps understand:

RAG architecture
Vector embeddings
Semantic search
Chunking strategies
Vector databases
Modular AI application design
