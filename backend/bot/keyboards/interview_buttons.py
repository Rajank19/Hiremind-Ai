from telegram import ReplyKeyboardMarkup


def get_difficulty_menu():

    keyboard = [
        ["Easy"],
        ["Medium"],
        ["Hard"],
        ["End Interview"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )