from typing import Annotated, List
from fastapi import FastAPI, Query
from pydantic import UUID4

from request.chats.chat import Chat
from services.chat_service import ChatService
from request.messages.create_message_request import CreateMessageRequest
from request.messages.list_messages_request import ListMessagesParams
from request.messages.message import Message
from services.message_service import MessageService

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
def current_chat() -> Chat | None:
    user_id = get_user_id()
    chat = ChatService.get_current_chat(user_id)

    return chat


@app.post("/v1/chats/{chat_id}/messages")
def create_message(chat_id: UUID4, request: CreateMessageRequest) -> Message:
    # TODO: Check if the chat_id belongs to the user.

    message = MessageService.create_message(chat_id, request.text)

    return message


@app.get("/v1/chats/{chat_id}/messages")
def list_messages(
    chat_id: UUID4, query_params: Annotated[ListMessagesParams, Query()]
) -> List[Message]:
    messages = MessageService.get_messages_for_chat(
        chat_id,
        query_params.sort_field,
        query_params.sort_direction,
        query_params.limit,
        query_params.offset,
    )
    return messages


# Stubbed because of prototype limitations.
@staticmethod
def get_user_id():
    return "6aafd72f-d85e-4f0f-a8f5-31d0adb311df"
