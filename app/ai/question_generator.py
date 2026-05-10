import json
import random


def get_question(domain, difficulty):

    file_path = f"data/questions/{domain.lower()}_questions.json"

    with open(file_path, "r", encoding="utf-8") as file:

        questions = json.load(file)

    filtered_questions = [
        q for q in questions
        if q["difficulty"] == difficulty
    ]

    selected_question = random.choice(filtered_questions)

    return selected_question