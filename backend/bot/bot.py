from telegram import Update

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from app.config.settings import BOT_TOKEN

from app.bot.handlers.start_handler import start_command
from app.bot.handlers.interview_handler import domain_handler
from app.bot.handlers.feedback_handler import difficulty_handler
from app.bot.handlers.report_handler import answer_handler
from app.bot.handlers.voice_handler import voice_handler

from app.services.analytics_service import (
    get_user_analytics,
    fetch_leaderboard
)


async def analytics_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    username = update.effective_user.username

    if username is None:

        username = update.effective_user.first_name

    results = get_user_analytics(username)

    if not results:

        await update.message.reply_text(
            "❌ No interview history found."
        )

        return

    message = "📊 Your Interview History\n\n"

    for row in results:

        domain, score, performance, created_at = row

        message += (
            f"🧠 Domain: {domain}\n"
            f"⭐ Score: {score}/10\n"
            f"🏆 Performance: {performance}\n"
            f"📅 Date: {created_at}\n\n"
        )

    await update.message.reply_text(message)


async def leaderboard_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    leaderboard = fetch_leaderboard()

    if not leaderboard:

        await update.message.reply_text(
            "❌ No leaderboard data found."
        )

        return

    message = "🏆 Top Interview Performers\n\n"

    rank = 1

    for row in leaderboard:

        username, avg_score = row

        message += (
            f"{rank}. {username} → {avg_score}/10\n"
        )

        rank += 1

    await update.message.reply_text(message)


def create_bot():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(start_command)

    app.add_handler(domain_handler)

    app.add_handler(difficulty_handler)

    app.add_handler(answer_handler)

    app.add_handler(voice_handler)

    app.add_handler(
        CommandHandler(
            "analytics",
            analytics_command
        )
    )

    app.add_handler(
        CommandHandler(
            "leaderboard",
            leaderboard_command
        )
    )

    return app