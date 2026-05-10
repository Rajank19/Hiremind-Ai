from telegram import Update

from telegram.ext import (
    MessageHandler,
    filters,
    ContextTypes
)

from app.services.voice_service import (
    convert_voice_to_text
)

from app.ai.evaluator import (
    evaluate_answer
)

from app.ai.feedback_generator import (
    generate_ai_feedback
)


async def handle_voice(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    voice = update.message.voice

    file = await context.bot.get_file(
        voice.file_id
    )

    file_path = "voice_answer.ogg"

    await file.download_to_drive(
        file_path
    )

    try:

        text = convert_voice_to_text(
            file_path
        )

        expected_answer = context.user_data.get(
            "expected_answer",
            ""
        )

        score, _ = evaluate_answer(
            text,
            expected_answer
        )

        feedback = generate_ai_feedback(
            score
        )

        await update.message.reply_text(
            f"🎤 Voice Answer Detected\n\n"
            f"📝 Converted Text:\n{text}\n\n"
            f"⭐ Score: {score}/10\n\n"
            f"🤖 Feedback:\n{feedback}"
        )

    except Exception as e:

        await update.message.reply_text(
            f"❌ Voice processing failed.\n\n{e}"
        )


voice_handler = MessageHandler(
    filters.VOICE,
    handle_voice
)