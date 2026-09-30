from .gemini_client import ask_gemini


def get_learning_recommendations(topic: str) -> str:
    if not topic.strip():
        return "Please enter a topic."

    prompt = f"""
Create a personalized learning path for this topic:

{topic}

Structure it as:
1. Beginner foundations
2. Intermediate concepts
3. Advanced concepts
4. Suggested practice/projects
5. Useful resource types such as documentation, videos, articles, or books
6. A simple 4-week study schedule

Keep the plan realistic for a student.
"""
    return ask_gemini(prompt)
