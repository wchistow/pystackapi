from typing import Any

from .base import BaseModel, SiteT


class Badge(BaseModel):
    """Implements the badge object - https://api.stackexchange.com/docs/types/badge."""
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)
