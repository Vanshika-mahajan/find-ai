import chromadb

# persistent storage
client = chromadb.PersistentClient(path="vector_db")

collection = client.get_or_create_collection("documents")


def store_embeddings(chunks, embeddings):

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )


def search(query_embedding, top_k=3):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]