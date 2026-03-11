import chromadb

# persistent storage
client = chromadb.PersistentClient(path="vector_db")

collection = client.get_or_create_collection("documents")


def store_embeddings(chunks, embeddings, source):

    ids = [f"{source}_{i}" for i in range(len(chunks))]

    metadata = [{"source": source} for _ in chunks]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadata
    )


def search(query_embedding, top_k=3):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]
    ids = results["ids"][0]

    return documents, ids