from langchain_community.vectorstores import FAISS
from models.embeddings import get_embedding_model


def create_vector_store(documents):
    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        documents,
        embeddings
    )

    return vector_store


def retrieve_documents(vector_store, query):
    docs = vector_store.similarity_search(
        query,
        k=3
    )

    return docs
