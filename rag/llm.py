import subprocess


def generate_answer(context_chunks, question):

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are an intelligent assistant helping users understand company documents.

Use ONLY the information provided in the context to answer the question.
If the answer is not present in the context, say:
"I cannot find the answer in the provided documents."

Provide clear and concise answers.

Context:
{context}

Question:
{question}

Answer:
"""

    result = subprocess.run(
        ["ollama", "run", "phi"],
        input=prompt,
        text=True,
        encoding="utf-8",
        capture_output=True
    )

    return result.stdout