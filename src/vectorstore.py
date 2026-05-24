from langchain_community.vectorstores import Chroma

def create_vector_db(chunks, embedding_model):
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="../vectorstore"
    )

    print("Vector DB created")
    return vector_db