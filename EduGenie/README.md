# EduGenie - Gemini Powered Learning Assistant

EduGenie is a FastAPI + HTML/CSS educational assistant based on the project description provided in the accompanying document.

Features:
- Ask questions
- Explain topics
- Generate 3 MCQs
- Summarize educational text
- Generate a beginner-to-advanced learning path

## 1. Requirements

Install Python 3.10 or newer.

## 2. Create a virtual environment

Windows PowerShell:

    py -3.11 -m venv .venv
    .\.venv\Scripts\Activate.ps1

If PowerShell blocks activation, run:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Then activate again.

## 3. Install packages

    python -m pip install --upgrade pip
    pip install -r requirements.txt

## 4. Configure Gemini

Create a Gemini API key in Google AI Studio.

Copy .env.example to .env and put your key in:

    GEMINI_API_KEY=your_key_here

Do NOT upload .env to GitHub.

## 5. Run the application

    uvicorn main:app --reload

Open:

    http://127.0.0.1:8000

FastAPI documentation:

    http://127.0.0.1:8000/docs

## 6. If the server does not start

Make sure your terminal is inside the EduGenie project folder:

    cd path\to\EduGenie

Then:

    .\.venv\Scripts\Activate.ps1
    python -m uvicorn main:app --reload

## Project structure

EduGenie/
    main.py
    requirements.txt
    .env.example
    .gitignore
    README.md
    modules/
        __init__.py
        gemini_client.py
        qna.py
        explanation.py
        quiz.py
        summary.py
        learning_path.py
    templates/
        index.html
    static/
        style.css
