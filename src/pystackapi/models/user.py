from typing import Any

from .base import BaseModel, SiteT
from .answer import Answer
from .badge import Badge


class User(BaseModel):
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)

    def get_answers(self, **kwargs: Any) -> list[Answer]:
        response = self._client.call(f'users/{self.account_id}/answers', **kwargs)
        return [Answer(self._client, dict(data)) for data in response]

    def get_badges(self, **kwargs: Any) -> list[Badge]:
        response = self._client.call(f'users/{self.account_id}/badges', **kwargs)
        return [Badge(self._client, dict(data)) for data in response]
