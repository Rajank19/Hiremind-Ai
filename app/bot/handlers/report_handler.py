from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes

from app.ai.evaluator import evaluate_answer

from app.ai.feedback_generator import (
    generate_ai_feedback
)

from app.bot.keyboards.interview_buttons import (
    get_difficulty_menu
)


async def handle_answer(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    ignored_buttons = [
        "Python",
        "React",
        "JavaScript",
        "DBMS",
        "AI/ML",
        "Easy",
        "Medium",
        "Hard",
        "End Interview"
    ]

    if text not in ignored_buttons:

        expected_answer = context.user_data.get(
            "expected_answer",
            ""
        )

        score, _ = evaluate_answer(
            text,
            expected_answer
        )

        feedback = generate_ai_feedback(score)

        if "scores" not in context.user_data:

            context.user_data["scores"] = []

        context.user_data["scores"].append(score)

        await update.message.reply_text(
            f"📊 Interview Feedback\n\n"
            f"⭐ Score: {score}/10\n\n"
            f"📝 Feedback: {feedback}\n\n"
            f"📘 Expected Answer:\n"
            f"{expected_answer}\n\n"
            f"🎯 Choose next difficulty level:",
            reply_markup=get_difficulty_menu()
        )


answer_handler = MessageHandler(
    filters.TEXT & ~filters.COMMAND,
    handle_answer
)