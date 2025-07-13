import sqlite3
from typing import List
import uuid

from assistant.assistant_orchestrator import AssistantOrchestrator
from config import settings
from datetime import datetime, timezone

from request.messages.list_messages_request import SortDirection, SortField
from request.messages.message import Message

DATABASE_FILE = settings.database_file


class MessageService:
    @staticmethod
    def create_message(chat_id: uuid.UUID, user_text: str) -> Message:
        """Get's the response for a user's query and persists the entire Message in the database.

        Before getting a response, finds the latest response ID for the Chat to maintain conversation context.

        Args:
            chat_id: The id of the Chat to create the message
            user_text: The user's query.

        Returns:
            The created Message with the response populated.
        """
        with sqlite3.connect(settings.database_file) as connection:
            cursor = connection.cursor()

            timestamp = datetime.now(timezone.utc)
            id = uuid.uuid4()
            message = Message(
                id=id,
                chat_id=chat_id,
                created_at=timestamp,
                user_text=user_text,
                is_terminal=False,
            )

            # Get the latest response ID from the Chat to maintain conversation context.
            latest_response_id = MessageService.get_latest_response_id(chat_id)
            response_text, response_id = AssistantOrchestrator.get_response(
                message, latest_response_id
            )
            message.response_text = response_text

            insert_statement = """
                INSERT INTO Messages(id, chat_id, user_text, created_at, response_text, openai_response_id, is_terminal) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            insert_data = (
                str(id),
                str(chat_id),
                user_text,
                timestamp,
                message.response_text,
                response_id,
                message.is_terminal,
            )
            cursor.execute(insert_statement, insert_data)
            connection.commit()

            return message

    @staticmethod
    def get_messages_for_chat(
        chat_id: uuid.UUID,
        sort_field: SortField,
        sort_direction: SortDirection,
        limit: int,
        offset: int = 0,
    ) -> List[Message]:
        """Get's messages from a specific Chat.

        Args:
            chat_id: The id of the Chat to get messages from.
            sort_field: What field to sort on.
            sort_direction: What direction to sort.
            limit: The maximum number of Messages to get.
            offset: When paginating, the row to start counting from.

        Returns:
            A list of Messages.
        """

        with sqlite3.connect(settings.database_file) as connection:
            cursor = connection.cursor()

            order_by = f"{sort_field.value} {'ASC' if sort_direction == SortDirection.ascending else 'DESC'}"

            select_statement = f"""
                SELECT id, chat_id, user_text, created_at, response_text, moderation_code, is_terminal
                FROM Messages
                WHERE chat_id=?
                ORDER BY {order_by}
                LIMIT ?
                OFFSET ?
            """
            select_data = (str(chat_id), limit, offset)

            result = cursor.execute(select_statement, select_data)
            rows = result.fetchall()

            messages = [
                Message(
                    id=row[0],
                    chat_id=row[1],
                    user_text=row[2],
                    created_at=row[3],
                    response_text=row[4],
                    moderation_code=row[5],
                    is_terminal=row[6],
                )
                for row in rows
            ]

            return messages

    @staticmethod
    def get_latest_response_id(chat_id: uuid.UUID) -> str | None:
        """Gets the openai_response_id of the latest Message in a chat (based on created_at timestamp).

        Args:
            chat_id: The id of the Chat to get the latest response ID from.

        Returns:
            The openai_response_id of the latest message in the Chat, or None if none was present.
        """
        with sqlite3.connect(settings.database_file) as connection:
            cursor = connection.cursor()

            select_statement = """
                SELECT openai_response_id
                FROM Messages
                WHERE chat_id=?
                ORDER BY created_at DESC
                LIMIT 1
            """
            select_data = (str(chat_id),)

            response = cursor.execute(select_statement, select_data)
            row = response.fetchone()
            if row:
                return row[0]
            else:
                return None
