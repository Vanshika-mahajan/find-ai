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

    return "Documents indexed successfully"


def chat(message, history):

    docs, ids = retrieve(message)

    answer = generate_answer(docs, message, ids)

    return answer


with gr.Blocks(
    theme=gr.themes.Soft(),
    title="FIND AI"
) as demo:

    gr.Markdown(
        """
        #  FIND AI  
        ### Intelligent Document Assistant
        Upload company documents and ask questions instantly.
        """
    )

    with gr.Row():

        with gr.Column(scale=1):

            gr.Markdown("##  Document Upload")

            files = gr.File(
                label="Upload PDFs / Markdown",
                file_count="multiple"
            )

            process_btn = gr.Button(" Index Documents")

            status = gr.Textbox(
                label="System Status",
                value="Waiting for documents..."
            )

            process_btn.click(
                process_document,
                inputs=files,
                outputs=status
            )

        with gr.Column(scale=3):

            gr.Markdown("##  Chat with your knowledge base")

            chat_ui = gr.ChatInterface(
                fn=chat,
                chatbot=gr.Chatbot(height=500),
                textbox=gr.Textbox(
                    placeholder="Ask something about your documents..."
                )
            )

demo.launch()