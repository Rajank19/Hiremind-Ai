# # from fastapi import FastAPI
# # from fastapi.middleware.cors import CORSMiddleware

# # from app.database.models import create_tables
# # from app.database.queries import (
# #     save_interview_result,
# #     get_user_history,
# #     get_leaderboard
# # )

# # from app.ai.question_generator import get_question
# # from app.ai.evaluator import evaluate_answer

# # app = FastAPI()


# # # 🔥 CREATE TABLE ON START
# # @app.on_event("startup")
# # def startup():
# #     print("🚀 Starting App...")
# #     create_tables()


# # # ✅ CORS (React fix)
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )


# # # ✅ HOME
# # @app.get("/")
# # def home():
# #     return {"message": "HireMind API running"}


# # # ✅ GET QUESTION
# # @app.get("/question")
# # def get_interview_question(domain: str, difficulty: str):
# #     return get_question(domain, difficulty)


# # # ✅ SUBMIT ANSWER + SAVE TO DB
# # @app.post("/answer")
# # def submit_answer(answer: str, expected_answer: str, username: str, domain: str):

# #     print("🔥 ANSWER API HIT")
# #     print("USERNAME:", username)
# #     print("DOMAIN:", domain)

# #     score, feedback = evaluate_answer(answer, expected_answer)

# #     print("👉 SAVING TO DB...")

# #     save_interview_result(
# #         username=username,
# #         domain=domain,
# #         score=score,
# #         performance=feedback
# #     )

# #     print("✅ SAVED SUCCESSFULLY")

# #     return {
# #         "score": score,
# #         "feedback": feedback
# #     }


# # # ✅ USER HISTORY
# # @app.get("/history")
# # def user_history(username: str):
# #     data = get_user_history(username)

# #     formatted = [
# #         [item[0], item[1], item[2], item[3]]
# #         for item in data
# #     ]

# #     print("📊 HISTORY:", formatted)
# #     return formatted


# # # ✅ LEADERBOARD
# # @app.get("/leaderboard")
# # def leaderboard():
# #     data = get_leaderboard()

# #     formatted = [
# #         {
# #             "username": item[0],
# #             "score": item[1]
# #         }
# #         for item in data
# #     ]

# #     print("🏆 LEADERBOARD:", formatted)
# #     return formatted
# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware

# # ✅ DATABASE
# from app.database.models import create_tables
# from app.database.queries import (
#     save_interview_result,
#     get_user_history,
#     get_leaderboard
# )

# # ✅ AI
# from app.ai.question_generator import get_question
# from app.ai.evaluator import evaluate_answer

# # ✅ PDF FEATURE
# from app.services.pdf_question_service import extract_questions_from_pdf


# app = FastAPI()


# # 🔥 STARTUP
# @app.on_event("startup")
# def startup():
#     print("🚀 Starting App...")
#     create_tables()


# # ✅ CORS (React fix)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# # ✅ HOME
# @app.get("/")
# def home():
#     return {"message": "HireMind API running"}


# # ✅ GET QUESTION (AI MODE)
# @app.get("/question")
# def get_interview_question(domain: str, difficulty: str):
#     return get_question(domain, difficulty)


# # ✅ SUBMIT ANSWER + SAVE TO DB
# @app.post("/answer")
# def submit_answer(answer: str, expected_answer: str, username: str, domain: str):

#     print("🔥 ANSWER API HIT")
#     print("USERNAME:", username)
#     print("DOMAIN:", domain)

#     score, feedback = evaluate_answer(answer, expected_answer)

#     print("👉 SAVING TO DB...")

#     save_interview_result(
#         username=username,
#         domain=domain,
#         score=score,
#         performance=feedback
#     )

#     print("✅ SAVED SUCCESSFULLY")

#     return {
#         "score": score,
#         "feedback": feedback
#     }


# # ✅ PDF QUESTION BANK (NEW 🔥)
# @app.post("/pdf-question-bank")
# def pdf_question_bank(file: UploadFile = File(...)):

#     print("📄 PDF UPLOADED")

#     questions = extract_questions_from_pdf(file.file)

#     print("✅ QUESTIONS EXTRACTED:", len(questions))

#     return {
#         "total": len(questions),
#         "questions": questions
#     }


# # ✅ USER HISTORY
# @app.get("/history")
# def user_history(username: str):

#     data = get_user_history(username)

#     formatted = [
#         [item[0], item[1], item[2], item[3]]
#         for item in data
#     ]

#     print("📊 HISTORY:", formatted)

#     return formatted


# # ✅ LEADERBOARD
# @app.get("/leaderboard")
# def leaderboard():

#     data = get_leaderboard()

#     formatted = [
#         {
#             "username": item[0],
#             "score": item[1]
#         }
#         for item in data
#     ]

#     print("🏆 LEADERBOARD:", formatted)

#     return formatted

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

# ✅ DATABASE
from app.database.models import create_tables
from app.database.queries import (
    save_interview_result,
    get_user_history,
    get_leaderboard
)

# ✅ AI
from app.ai.question_generator import get_question
from app.ai.evaluator import evaluate_answer

# ✅ PDF FEATURE
from app.services.pdf_question_service import extract_questions_from_pdf


app = FastAPI()

# 🔥 GLOBAL VARIABLES (PDF INTERVIEW FLOW)
current_index = 0
questions_store = []


# 🔥 STARTUP
@app.on_event("startup")
def startup():
    print("🚀 Starting App...")
    create_tables()


# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===============================
# 🏠 HOME
# ===============================
@app.get("/")
def home():
    return {"message": "HireMind API running"}


# ===============================
# 🎯 AI INTERVIEW MODE
# ===============================

@app.get("/question")
def get_interview_question(domain: str, difficulty: str):
    return get_question(domain, difficulty)


@app.post("/answer")
def submit_answer(answer: str, expected_answer: str, username: str, domain: str):

    score, feedback = evaluate_answer(answer, expected_answer)

    save_interview_result(
        username=username,
        domain=domain,
        score=score,
        performance=feedback
    )

    return {
        "score": score,
        "feedback": feedback
    }


# ===============================
# 📄 PDF QUESTION BANK MODE
# ===============================

@app.post("/pdf-question-bank")
def pdf_question_bank(file: UploadFile = File(...)):

    global questions_store, current_index

    questions_store = extract_questions_from_pdf(file.file)
    current_index = 0

    return {
        "message": "Interview Started",
        "total_questions": len(questions_store)
    }


# ✅ GET FIRST / NEXT QUESTION
@app.get("/next-question")
def next_question():

    global current_index, questions_store

    if len(questions_store) == 0:
        return {"error": "No questions loaded. Upload PDF first."}

    if current_index >= len(questions_store):
        return {"message": "Interview Finished"}

    q = questions_store[current_index]

    return {
        "question_number": current_index + 1,
        "question": q["question"]
    }


# ✅ SUBMIT ANSWER + AUTO NEXT
@app.post("/submit-pdf-answer")
def submit_pdf_answer(answer: str):

    global current_index, questions_store

    if len(questions_store) == 0:
        return {"error": "No questions loaded. Upload PDF first."}

    if current_index >= len(questions_store):
        return {"message": "Interview already finished"}

    # 👉 current question
    q = questions_store[current_index]

    # 👉 evaluate
    score, feedback = evaluate_answer(answer, q["answer"])

    # 👉 move next
    current_index += 1

    # 👉 if finished
    if current_index >= len(questions_store):
        return {
            "score": score,
            "feedback": feedback,
            "message": "Interview Finished"
        }

    # 👉 next question
    next_q = questions_store[current_index]

    return {
        "score": score,
        "feedback": feedback,
        "next_question": next_q["question"],
        "next_question_number": current_index + 1
    }


# ===============================
# 📊 HISTORY
# ===============================

@app.get("/history")
def user_history(username: str):

    data = get_user_history(username)

    return [
        [item[0], item[1], item[2], item[3]]
        for item in data
    ]


# ===============================
# 🏆 LEADERBOARD
# ===============================

@app.get("/leaderboard")
def leaderboard():

    data = get_leaderboard()

    return [
        {
            "username": item[0],
            "score": item[1]
        }
        for item in data
    ]