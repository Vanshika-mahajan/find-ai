import gradio as gr
from rag.loader import load_document
from rag.chunker import chunk_text
from rag.embeddings import create_embeddings
from rag.vectordb import store_embeddings
from rag.retriever import retrieve
from rag.llm import generate_answer


def process_document(files):

    for file in files:

        text = load_document(file.name)

        chunks = chunk_text(text)

        embeddings = create_embeddings(chunks)

        store_embeddings(chunks, embeddings, file.name)

    return "All documents processed successfully!"


def chat(message, history):

    docs, ids = retrieve(message)

    answer = generate_answer(docs, message, ids)
    return answer


with gr.Blocks() as demo:

    gr.Markdown("# FIND AI - Intelligent Document Assistant")

    with gr.Row():
        files = gr.File(label="Upload PDFs", file_count="multiple")
        process_btn = gr.Button("Process Document")

    status = gr.Textbox(label="Status")

    process_btn.click(process_document, inputs=files, outputs=status)

    gr.Markdown("## Chat with your document")

    chat_ui = gr.ChatInterface(fn=chat)

demo.launch()