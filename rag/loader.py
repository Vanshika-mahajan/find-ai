from pypdf import PdfReader


def load_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF document.

    Args:
        file_path (str): path to the pdf file

    Returns:
        str: full extracted text
    """

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text