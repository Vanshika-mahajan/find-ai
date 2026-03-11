import subprocess
import os


def generate_answer(context_chunks, question, sources):

    context = "\n\n".join(context_chunks)

    prompt = f"""
Answer the question using ONLY the context below.

If the answer cannot be found in the context, say:
"The answer is not present in the provided documents."

Context:
{context}

Question: {question}

Answer in 2–4 sentences:
"""
    print("\n--- CONTEXT SENT TO LLM ---\n")
    print(context[:1000])

    result = subprocess.run(
        ["ollama", "run", "llama3.2"],
        input=prompt,
        text=True,
        encoding="utf-8",
        capture_output=True
    )

    answer = result.stdout.strip()

    source_text = "\n\nSources:\n"

    for s in sources:
        filename = os.path.basename(s)

        if "_" in filename:
            doc, chunk = filename.rsplit("_", 1)
            source_text += f"• {doc} (Chunk {chunk})\n"
        else:
            source_text += f"• {filename}\n"

    return answer + source_text