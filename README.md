# find-ai

FIND AI – A Retrieval-Augmented Intelligent Document Assistant built using open-source LLMs, vector search, and semantic retrieval.
FIND AI is a Retrieval-Augmented Generation (RAG) based intelligent document assistant.

The system allows users to upload documents and ask natural language questions.
Relevant information is retrieved using semantic embeddings and vector similarity search,
and responses are generated using a local LLM.

## Tech Stack

- Python
- Gradio
- Sentence Transformers
- ChromaDB
- Ollama (Local LLM)
- PyPDF

## Architecture

User → Gradio UI → Document Loader → Chunking → Embeddings → Vector DB → Retriever → LLM → Answer
