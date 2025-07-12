import sqlite3
from uuid import uuid4
from config import settings
from datetime import datetime, timezone

from request.chats.chat import Chat

DATABASE_FILE = settings.database_file


class ChatService:
    # Automatically sets any currently active chats to inactive.
    @staticmethod
    def insert_chat(user_id) -> Chat:
        with sqlite3.connect(settings.database_file) as connection:
            cursor = connection.cursor()

            # Set all current chats to inactive.
            update_statement = """
                UPDATE Chats 
                SET is_active=false 
                WHERE user_id=?
            """
            update_data = (user_id,)
            cursor.execute(update_statement, update_data)

            # Insert a new chat with is_active=True
            insert_statement = """
                INSERT INTO Chats(id, user_id, is_active, created_at) 
                VALUES (?, ?, ?, ?)
            """

            id = uuid4()
            timestamp = datetime.now(timezone.utc)
            insert_data = (str(id), user_id, True, timestamp)

            cursor.execute(insert_statement, insert_data)
            connection.commit()

            return Chat(id=id, is_active=True, created_at=timestamp)

    @staticmethod
    def get_current_chat(user_id) -> Chat | None:
        with sqlite3.connect(settings.database_file) as connection:
            cursor = connection.cursor()

            select_statement = """
                SELECT id, is_active, created_at 
                FROM Chats 
                WHERE user_id=? 
                    AND is_active=true LIMIT 1
            """
            select_data = (user_id,)
            response = cursor.execute(select_statement, select_data)
            row = response.fetchone()

            if row:
                return Chat(
                    id=row[0], is_active=row[1], created_at=row[2], user_id=user_id
                )
            else:
                return None
