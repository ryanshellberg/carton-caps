from pydantic import BaseModel


class CreateMessageRequest(BaseModel):
    text: str
