from app.bot.bot import create_bot

from app.database.models import create_tables


def main():

    create_tables()

    app = create_bot()

    print("✅ HireMind AI Bot Running...")

    app.run_polling()


if __name__ == "__main__":

    main()