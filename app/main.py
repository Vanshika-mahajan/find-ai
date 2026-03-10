from rag.loader import load_pdf
from rag.chunker import chunk_text
from rag.embeddings import create_embeddings
from rag.vectordb import store_embeddings
from rag.retriever import retrieve
from rag.llm import generate_answer

# Load document
text = load_pdf("data/sample.pdf")

# Split into chunks
chunks = chunk_text(text)

# Generate embeddings
embeddings = create_embeddings(chunks)

# Store in vector database
store_embeddings(chunks, embeddings)

print("Chunks stored in vector database:", len(chunks))


# ---- TEST RETRIEVAL ----
query = "What is this document about?"

results = retrieve(query)

print("\nTop retrieved chunks:\n")

for r in results:
    print(r[:200])
    print("----")

query = "What is the objective of the program?"

results = retrieve(query)

answer = generate_answer(results, query)

print("\nAI Answer:\n")
print(answer)