from enum import Enum
from pydantic import BaseModel


class SortField(str, Enum):
    created_at = "created_at"


class SortDirection(str, Enum):
    ascending = "ascending"
    descending = "descending"


class ListMessagesParams(BaseModel):
    limit: int = 50
    offset: int = 0
    sort_field: SortField = SortField.created_at
    sort_direction: SortDirection = SortDirection.descending
