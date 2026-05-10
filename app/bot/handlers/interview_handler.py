from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes

from app.database.queries import save_interview_result

from app.bot.keyboards.interview_buttons import (
    get_difficulty_menu
)

from app.services.report_service import (
    generate_pdf_report
)


async def handle_domain(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    domains = [
        "Python",
        "React",
        "JavaScript",
        "DBMS",
        "AI/ML"
    ]

    if text in domains:

        context.user_data["domain"] = text

        await update.message.reply_text(
            f"🔥 You selected {text}\n\n"
            "Choose Difficulty Level:",
            reply_markup=get_difficulty_menu()
        )

    elif text == "End Interview":

        scores = context.user_data.get(
            "scores",
            []
        )

        total_questions = len(scores)

        if total_questions > 0:

            average_score = round(
                sum(scores) / total_questions,
                1
            )

        else:

            average_score = 0

        if average_score >= 8:

            performance = "Excellent"

        elif average_score >= 6:

            performance = "Good"

        elif average_score >= 4:

            performance = "Average"

        else:

            performance = "Needs Improvement"

        username = update.effective_user.username

        if username is None:

            username = update.effective_user.first_name

        print("SAVE USERNAME:", username)

        domain = context.user_data.get(
            "domain",
            "Unknown"
        )

        save_interview_result(
            username,
            domain,
            average_score,
            performance
        )

        pdf_file = generate_pdf_report(
            username,
            domain,
            average_score,
            performance
        )

        await update.message.reply_text(
            f"📊 Final Interview Report\n\n"
            f"✅ Questions Attempted: {total_questions}\n"
            f"⭐ Average Score: {average_score}/10\n"
            f"🏆 Performance Level: {performance}\n\n"
            f"🚀 Keep practicing and improving your interview skills!"
        )

        with open(pdf_file, "rb") as pdf:

            await update.message.reply_document(
                document=pdf,
                filename=pdf_file,
                caption="📄 Your Interview Report"
            )

        context.user_data.clear()


domain_handler = MessageHandler(
    filters.Regex(
        "^(Python|React|JavaScript|DBMS|AI/ML|End Interview)$"
    ),
    handle_domain
)