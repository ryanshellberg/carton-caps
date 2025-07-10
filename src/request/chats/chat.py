from datetime import datetime
from pydantic import UUID4, BaseModel


class Chat(BaseModel):
    id: UUID4
    is_active: bool = False
    created_at: datetime
