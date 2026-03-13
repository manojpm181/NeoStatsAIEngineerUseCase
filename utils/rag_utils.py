from langchain_community.vectorstores import FAISS
from models.embeddings import get_embedding_model


def create_vector_store(documents):

    embeddings = get_embedding_model()

    vectorstore = FAISS.from_documents(
        documents,
        embeddings
    )

    return vectorstore


def retrieve_documents(vectorstore, query):

    docs = vectorstore.similarity_search(
        query,
        k=3
    )

    return docs