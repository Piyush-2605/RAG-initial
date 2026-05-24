


def search_documents(vector_db, query):

    results = vector_db.similarity_search(query, k=6)

    return results    