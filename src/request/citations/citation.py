from typing import Optional
from pydantic import UUID4, BaseModel


class Citation(BaseModel):
    id: UUID4
    name: str
    url: Optional[str] = None
