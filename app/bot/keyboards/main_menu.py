from telegram import ReplyKeyboardMarkup


def get_main_menu():

    keyboard = [
        ["Python", "React"],
        ["JavaScript", "DBMS"],
        ["AI/ML"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )