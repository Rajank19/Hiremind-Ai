from fastapi import FastAPI
from app.database.models import create_tables
from app.ai.question_generator import get_question
from app.ai.evaluator import evaluate_answer
from app.database.queries import (
    save_interview_result,
    get_user_history,
    get_leaderboard
)

app = FastAPI()


# 🔥 RUN ON STARTUP (DB + TABLE FIX)
@app.on_event("startup")
def startup():
    print("🚀 Starting App...")
    create_tables()


# ✅ HOME
@app.get("/")
def home():
    return {"message": "HireMind API running"}


# ✅ GET QUESTION
@app.get("/question")
def get_interview_question(domain: str, difficulty: str):
    return get_question(domain, difficulty)


@app.post("/answer")
def submit_answer(answer: str, expected_answer: str, username: str, domain: str):

    print("🔥🔥 API CALLED 🔥🔥")

    score, feedback = evaluate_answer(answer, expected_answer)

    print("👉 CALLING SAVE FUNCTION NOW")

    # 🔥 DIRECT PRINT INSIDE MAIN
    from app.database.db import connect_db

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO interview_history (username, domain, score, performance)
        VALUES (?, ?, ?, ?)
        """,
        (username, domain, score, feedback)
    )

    conn.commit()
    conn.close()

    print("✅ DATA SAVED FROM MAIN")

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