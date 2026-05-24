from src.loader import load_pdf
from src.splitter import split_documents
from src.embeddings import get_embedding_model
from src.vectorstore import create_vector_db
from src.retriever import search_documents

docs = load_pdf(r"C:\Users\Piyush\RAG\data\Paid Final Ultimate Workout Routine Of MMA Fighters.pdf")

chunks = split_documents(docs)

embedding_model = get_embedding_model()

vector_db = create_vector_db(chunks, embedding_model)

query = "how to inncrease speed?"

results = search_documents(vector_db, query)

for i, doc in enumerate(results):
    print(f"\nResult {i+1}:")
    print(doc.page_content[:300])