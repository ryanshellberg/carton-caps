from datetime import datetime
from typing import List, Optional
from pydantic import UUID4, BaseModel

from request.citations.citation import Citation
from request.messages.moderation_code import ModerationCode


class Message(BaseModel):
    id: UUID4
    chat_id: UUID4
    user_text: str
    response_text: Optional[str] = None
    response_citations: List[Citation] = []
    moderation_code: Optional[ModerationCode] = None
    is_terminal: bool
    created_at: datetime
