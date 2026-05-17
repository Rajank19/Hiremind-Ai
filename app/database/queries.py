from app.database.db import connect_db


# ✅ SAVE RESULT
def save_interview_result(username, domain, score, performance):

    print("🔥 SAVING DATA STARTED")

    connection = connect_db()
    cursor = connection.cursor()

    print("📁 DB PATH (SAVE):", connection)

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
        (username, domain, score, performance)
    )

    connection.commit()

    print("✅ DATA SAVED SUCCESSFULLY")

    connection.close()


# ✅ GET USER HISTORY
def get_user_history(username):

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT domain, score, performance, created_at
        FROM interview_history
        WHERE username = ?
        """,
        (username,)
    )

    results = cursor.fetchall()

    print("📊 USER HISTORY:", results)

    connection.close()

    return results


# ✅ GET LEADERBOARD
def get_leaderboard():

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT username, ROUND(AVG(score), 1) as avg_score
        FROM interview_history
        GROUP BY username
        ORDER BY avg_score DESC
        LIMIT 10
        """
    )

    results = cursor.fetchall()

    print("🏆 LEADERBOARD:", results)

    connection.close()

    return results