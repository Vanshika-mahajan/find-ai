import re


def chunk_markdown(text):

    sections = re.split(r"\n# ", text)

    chunks = []

    for section in sections:

        if len(section.strip()) == 0:
            continue

        chunk = "# " + section.strip()

        chunks.append(chunk)

    return chunks


def chunk_text(text, chunk_size=500):

    if "# " in text:
        return chunk_markdown(text)

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size

    return chunks