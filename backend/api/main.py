from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.models import create_tables
from app.database.queries import (
    save_interview_result,
    get_user_history,
    get_leaderboard
)

from app.ai.question_generator import get_question
from app.ai.evaluator import evaluate_answer

app = FastAPI()


# 🔥 CREATE TABLE ON START
@app.on_event("startup")
def startup():
    print("🚀 Starting App...")
    create_tables()


# ✅ CORS (React fix)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ✅ HOME
@app.get("/")
def home():
    return {"message": "HireMind API running"}


# ✅ GET QUESTION
@app.get("/question")
def get_interview_question(domain: str, difficulty: str):
    return get_question(domain, difficulty)


# ✅ SUBMIT ANSWER + SAVE TO DB
@app.post("/answer")
def submit_answer(answer: str, expected_answer: str, username: str, domain: str):

    print("🔥 ANSWER API HIT")
    print("USERNAME:", username)
    print("DOMAIN:", domain)

    score, feedback = evaluate_answer(answer, expected_answer)

    print("👉 SAVING TO DB...")

    save_interview_result(
        username=username,
        domain=domain,
        score=score,
        performance=feedback
    )

    print("✅ SAVED SUCCESSFULLY")

    return {
        "score": score,
        "feedback": feedback
    }


# ✅ USER HISTORY
@app.get("/history")
def user_history(username: str):
    data = get_user_history(username)

    formatted = [
        [item[0], item[1], item[2], item[3]]
        for item in data
    ]

    print("📊 HISTORY:", formatted)
    return formatted


# ✅ LEADERBOARD
@app.get("/leaderboard")
def leaderboard():
    data = get_leaderboard()

    formatted = [
        {
            "username": item[0],
            "score": item[1]
        }
        for item in data
    ]

    print("🏆 LEADERBOARD:", formatted)
    return formatted