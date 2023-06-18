from typing import Any
from .base import BaseModel, SiteT


class Comment(BaseModel):
    """Implements the comment object - https://api.stackexchange.com/docs/types/comment."""
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)
