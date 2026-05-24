

from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    print("Total chunks:", len(chunks))

    return chunks