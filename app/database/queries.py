from app.database.db import connect_db


def save_interview_result(
    username,
    domain,
    score,
    performance
):

    print("SAVING DATA...")

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO interview_history (
            username,
            domain,
            score,
            performance
        )

        VALUES (?, ?, ?, ?)
        """,
        (
            username,
            domain,
            score,
            performance
        )
    )

    connection.commit()

    print("DATA SAVED SUCCESSFULLY")

    connection.close()


def get_user_history(username):

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            domain,
            score,
            performance,
            created_at

        FROM interview_history

        WHERE username = ?
        """,
        (username,)
    )

    results = cursor.fetchall()

    print(results)

    connection.close()

    return results


def get_leaderboard():

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            username,
            ROUND(AVG(score), 1) AS avg_score

        FROM interview_history

        GROUP BY username

        ORDER BY avg_score DESC

        LIMIT 10
        """
    )

    results = cursor.fetchall()

    connection.close()

    return results