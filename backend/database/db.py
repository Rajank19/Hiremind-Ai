import sqlite3
import os

def connect_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    db_path = os.path.join(BASE_DIR, "hiremind.db")

    print("📁 DB PATH:", db_path)   # 🔥 DEBUG

    connection = sqlite3.connect(db_path)

    return connection