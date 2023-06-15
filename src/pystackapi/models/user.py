from typing import Any

from .base import BaseModel, SiteT
from .answer import Answer
from .badge import Badge
from .comment import Comment
from .priviledge import Privilege


class User(BaseModel):
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)

    def get_answers(self, **kwargs: Any) -> list[Answer]:
        response = self._client.call(f'users/{self.account_id}/answers', **kwargs)
        return [Answer(self._client, dict(data)) for data in response]

    def get_badges(self, **kwargs: Any) -> list[Badge]:
        response = self._client.call(f'users/{self.account_id}/badges', **kwargs)
        return [Badge(self._client, dict(data)) for data in response]

    def get_comments(self, toid: int | None = None, **kwargs: Any) -> list[Comment]:
        """Implements API methods `users/{ids}/comments` and `users/{ids}/comments/{toid}`."""
        if toid is not None:
            response = self._client.call(f'users/{self.account_id}/comments/{toid}', **kwargs)
        else:
            response = self._client.call(f'users/{self.account_id}/comments', **kwargs)
        return [Comment(self._client, dict(data)) for data in response]

    def get_privileges(self, **kwargs) -> list[Privilege]:
        response = self._client.call(f'users/{self.account_id}/privileges', **kwargs)
        return [Privilege(self._client, dict(data)) for data in response]
