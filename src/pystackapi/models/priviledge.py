from typing import Any

from .base import BaseModel, SiteT


class Privilege(BaseModel):
    """Implements the priviledge object - https://api.stackexchange.com/docs/types/privilege."""
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)
