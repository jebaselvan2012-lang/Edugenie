import json
import re

from .gemini_client import ask_gemini


def _clean_json(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def generate_quiz(passage: str):
    if not passage.strip():
        return {"error": "Please enter a topic or passage."}

    prompt = f"""
Create exactly 3 multiple-choice questions from the educational text below.

Text:
{passage}

Return ONLY valid JSON. No Markdown and no extra text.

JSON format:
[
  {{
    "question": "Question text",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

The answer field must contain exactly the option letter A, B, C, or D.
"""
    raw = ask_gemini(prompt)
    cleaned = _clean_json(raw)

    try:
        quiz = json.loads(cleaned)
        if not isinstance(quiz, list) or len(quiz) != 3:
            raise ValueError("Expected exactly 3 questions.")

        for item in quiz:
            if not all(k in item for k in ("question", "options", "answer")):
                raise ValueError("Invalid quiz item.")
            if len(item["options"]) != 4:
                raise ValueError("Each question must have 4 options.")
        return quiz
    except Exception as exc:
        return {
            "error": "Gemini returned an unexpected quiz format.",
            "details": str(exc),
            "raw_response": raw,
        }
