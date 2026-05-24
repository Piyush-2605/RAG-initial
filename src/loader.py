from langchain_community.document_loaders import PyPDFLoader

def load_pdf(path):

    loader = PyPDFLoader(path)

    documents = loader.load()

    print("Pages loaded:", len(documents))

    return documents