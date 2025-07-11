from datetime import datetime, timezone
from typing import Annotated
import uuid
from fastapi import FastAPI, Query
from pydantic import UUID4

from chats.chat_manager import ChatManager
from request.chats.chat import Chat
from services.chat_service import ChatService
from request.messages.create_message_request import CreateMessageRequest
from request.messages.list_messages_request import ListMessagesParams
from request.messages.message import Message

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/v1/chats")
def create_chat() -> Chat:
    user_id = get_user_id()
    chat = ChatService.insert_chat(user_id=user_id)
    return chat


@app.get("/v1/chats/current")
def current_chat() -> Chat:
    user_id = get_user_id()
    chat = ChatService.get_current_chat(user_id)
    return chat


@app.post("/v1/chats/{chat_id}/messages")
def create_message(chat_id: UUID4, request: CreateMessageRequest):
    timestamp = datetime.now(timezone.utc).isoformat()
    message = Message(
        id=uuid.uuid4(),
        chat_id=chat_id,
        created_at=timestamp,
        is_terminal=False,
        moderation_code=None,
        response_citations=[],
        user_text=request.text,
    )

    ChatManager.populate_response(message)

    return message


@app.get("/v1/chats/{chat_id}/messages")
def list_messages(chat_id: UUID4, query_params: Annotated[ListMessagesParams, Query()]):
    timestamp = datetime.now(timezone.utc).isoformat()
    message = Message(
        id=uuid.uuid4(),
        chat_id=chat_id,
        created_at=timestamp,
        is_terminal=False,
        moderation_code=None,
        response_citations=[],
        response_text="Your response!",
        user_text="Some query!",
    )

    return [message]


# Stubbed because of prototype limitations.
@staticmethod
def get_user_id():
    return "6aafd72f-d85e-4f0f-a8f5-31d0adb311df"
