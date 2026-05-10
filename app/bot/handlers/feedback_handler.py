from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes

from app.ai.question_generator import get_question


async def handle_difficulty(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    difficulties = ["Easy", "Medium", "Hard"]

    if text in difficulties:

        context.user_data["difficulty"] = text

        selected_domain = context.user_data.get(
            "domain",
            "Python"
        )

        question_data = get_question(
            selected_domain,
            text
        )

        question = question_data["question"]

        expected_answer = question_data.get(
            "expected_answer",
            ""
        )

        context.user_data["current_question"] = question

        context.user_data["expected_answer"] = expected_answer

        await update.message.reply_text(
            f"✅ Difficulty Selected: {text}\n\n"
            f"🧠 {selected_domain} Interview Question:\n\n"
            f"{question}\n\n"
            f"✍️ Type your answer below:"
        )


difficulty_handler = MessageHandler(
    filters.Regex("^(Easy|Medium|Hard)$"),
    handle_difficulty
)