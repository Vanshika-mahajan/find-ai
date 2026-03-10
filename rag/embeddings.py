from fastembed import TextEmbedding

# load embedding model
embedding_model = TextEmbedding()


def create_embeddings(chunks):
    """
    Convert text chunks into embedding vectors
    """

    embeddings = list(embedding_model.embed(chunks))

    return embeddings