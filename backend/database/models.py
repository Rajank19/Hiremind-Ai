from app.database.db import connect_db

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interview_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        domain TEXT,
        score INTEGER,
        performance TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

    print("✅ TABLE CREATED")