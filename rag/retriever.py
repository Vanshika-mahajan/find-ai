from rag.embeddings import create_embeddings
from rag.vectordb import collection


def retrieve(query, top_k=3):
    """
    Retrieve the most relevant chunks for a user query
    """

    # convert query to embedding
    query_embedding = create_embeddings([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]