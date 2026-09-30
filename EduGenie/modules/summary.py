from .gemini_client import ask_gemini


def summarize_text(text: str) -> str:
    if not text.strip():
        return "Please enter text to summarize."

    prompt = f"""
Summarize the following educational text for a student.

Text:
{text}

Requirements:
- Keep the important facts.
- Remove repetition.
- Use short paragraphs or bullet points.
- Do not invent information.
"""
    return ask_gemini(prompt)
