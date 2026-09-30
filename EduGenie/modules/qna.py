from .gemini_client import ask_gemini


def answer_question(question: str) -> str:
    if not question.strip():
        return "Please enter a question."

    prompt = f"""
You are EduGenie, a friendly educational assistant.
Answer the student's question clearly and accurately.

Question:
{question}

Rules:
- Use simple language.
- Give the direct answer first.
- Add a short explanation or example when useful.
- If the question is ambiguous, state the assumption.
"""
    return ask_gemini(prompt)
