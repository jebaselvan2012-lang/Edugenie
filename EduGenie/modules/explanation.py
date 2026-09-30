from .gemini_client import ask_gemini


def explain_topic(topic: str) -> str:
    if not topic.strip():
        return "Please enter a topic."

    prompt = f"""
You are EduGenie, an educational tutor.
Explain the following topic for a beginner:

Topic:
{topic}

Use:
1. Simple definition
2. Key idea
3. Easy example
4. Short recap

Avoid unnecessary jargon.
"""
    return ask_gemini(prompt)
