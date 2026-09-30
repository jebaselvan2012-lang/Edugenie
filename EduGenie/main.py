from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from modules.qna import answer_question
from modules.explanation import explain_topic
from modules.quiz import generate_quiz
from modules.summary import summarize_text
from modules.learning_path import get_learning_recommendations

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="EduGenie - Gemini Learning Assistant")

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


class TextRequest(BaseModel):
    text: str


class QuestionRequest(BaseModel):
    question: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"result": None},
    )


@app.post("/qa")
async def qa(data: QuestionRequest):
    return {"result": answer_question(data.question)}


@app.post("/explain")
async def explain(data: TextRequest):
    return {"result": explain_topic(data.text)}


@app.post("/quiz")
async def quiz(data: TextRequest):
    return {"result": generate_quiz(data.text)}


@app.post("/summarize")
async def summarize(data: TextRequest):
    return {"result": summarize_text(data.text)}


@app.post("/learn/recommendations")
async def learn(data: TextRequest):
    return {"result": get_learning_recommendations(data.text)}
