from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from app.bot.keyboards.main_menu import get_main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🚀 Welcome to HireMind AI\n\n"
        "Choose Interview Domain:",
        reply_markup=get_main_menu()
    )


start_command = CommandHandler("start", start)