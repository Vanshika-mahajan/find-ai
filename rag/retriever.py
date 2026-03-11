from rag.embeddings import create_embeddings
from rag.vectordb import collection,search

def retrieve(query, top_k=3):

    query_embedding = create_embeddings([query])[0]

    docs, ids = search(query_embedding, top_k)

    return docs, ids