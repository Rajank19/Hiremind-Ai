import sqlite3


def connect_db():

    connection = sqlite3.connect(
        "hiremind.db"
    )

    return connection