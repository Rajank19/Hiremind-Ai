# import json
# import random


# def get_question(domain, difficulty):

#     file_path = f"data/questions/{domain.lower()}_questions.json"

#     with open(file_path, "r", encoding="utf-8") as file:

#         questions = json.load(file)

#     filtered_questions = [
#         q for q in questions
#         if q["difficulty"] == difficulty
#     ]

#     selected_question = random.choice(filtered_questions)

#     return selected_question
import json
import random


def get_question(domain, difficulty):

    file_path = f"data/questions/{domain.lower()}_questions.json"

    with open(file_path, "r", encoding="utf-8") as file:
        questions = json.load(file)

    # 🔥 Safe filtering (case-insensitive + key check)
    filtered_questions = [
        q for q in questions
        if "difficulty" in q and q["difficulty"].lower() == difficulty.lower()
    ]

    # 🔥 Handle empty case (VERY IMPORTANT)
    if not filtered_questions:
        print("❌ No questions found")
        print("Difficulty given:", difficulty)
        print("Sample data:", questions[0])
        
        return {
            "question": "No questions found for this difficulty",
            "expected_answer": ""
        }

    selected_question = random.choice(filtered_questions)

    return selected_question