import sqlite3
import sys

sys.path.append("src")  # nopep8
from config import settings


def initialize():
    connection = sqlite3.connect(settings.database_file)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Chats (
        id TEXT PRIMARY KEY,
        user_id TEXT,
        is_active BOOLEAN NOT NULL,
        created_at TIMESTAMP NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Messages (
        id TEXT PRIMARY KEY,
        chat_id TEXT NOT NULL,
        user_text TEXT NOT NULL,
        response_text TEXT,
        openai_response_id TEXT,
        moderation_code TEXT,
        is_terminal BOOLEAN NOT NULL,
        created_at TIMESTAMP NOT NULL,
        FOREIGN KEY (chat_id) REFERENCES Chat(id) ON DELETE CASCADE
    );
    """)


if __name__ == "__main__":
    initialize()
