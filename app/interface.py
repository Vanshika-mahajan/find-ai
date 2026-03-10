import gradio as gr
from rag.loader import load_pdf
from rag.chunker import chunk_text
from rag.embeddings import create_embeddings
from rag.vectordb import store_embeddings
from rag.retriever import retrieve
from rag.llm import generate_answer


def process_document(file):

    text = load_pdf(file.name)

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    store_embeddings(chunks, embeddings)

    return "Document processed successfully!"


def chat(message, history):

    results = retrieve(message)

    answer = generate_answer(results, message)

    return answer


with gr.Blocks() as demo:

    gr.Markdown("# FIND AI - Intelligent Document Assistant")

    with gr.Row():
        file = gr.File(label="Upload PDF")
        process_btn = gr.Button("Process Document")

    status = gr.Textbox(label="Status")

    process_btn.click(process_document, inputs=file, outputs=status)

    gr.Markdown("## Chat with your document")

    chat_ui = gr.ChatInterface(fn=chat)

demo.launch()