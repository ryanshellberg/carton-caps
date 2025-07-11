import sqlite3
from uuid import uuid4
from config import settings
from datetime import datetime, timezone

from request.chats.chat import Chat

DATABASE_FILE = settings.database_file


class DatabaseClient:
    @staticmethod
    def insert_chat(user_id):
        with sqlite3.connect(settings.database_file) as connection:
            cursor = connection.cursor()

            insert_statement = """INSERT INTO Chats(id, user_id, is_active, created_at) VALUES (?, ?, ?, ?)"""

            id = uuid4()
            timestamp = datetime.now(timezone.utc).isoformat()
            data = (str(id), user_id, True, timestamp)

            cursor.execute(insert_statement, data)
            connection.commit()

            return Chat(id=id, is_active=True, created_at=timestamp)
