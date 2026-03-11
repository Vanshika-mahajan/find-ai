from pypdf import PdfReader
import os


def load_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def load_md(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_txt(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_document(file_path):

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return load_pdf(file_path)

    elif ext == ".md":
        return load_md(file_path)

    elif ext == ".txt":
        return load_txt(file_path)

    else:
        raise ValueError(f"Unsupported file type: {ext}")