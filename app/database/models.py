from app.database.db import connect_db


def create_tables():

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS interview_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            domain TEXT,

            score REAL,

            performance TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()

    connection.close()