from typing import Any, Type, TypeVar

from .base import BaseModel, SiteT
from .answer import Answer
from .badge import Badge
from .comment import Comment
from .priviledge import Privilege
from .question import Question


BaseModelT_co = TypeVar('BaseModelT_co', bound=BaseModel, covariant=True)


class User(BaseModel):
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)

    def _get_call(self, url: str, model: Type[BaseModelT_co], **kwargs: Any) -> list[BaseModelT_co]:
        response = self._client.call(url, **kwargs)
        return [model(self._client, dict(data)) for data in response]

    def get_answers(self, **kwargs: Any) -> list[Answer]:
        return self._get_call(f'users/{self.account_id}/answers', Answer, **kwargs)

    def get_badges(self, **kwargs: Any) -> list[Badge]:
        return self._get_call(f'users/{self.account_id}/badges', Badge, **kwargs)

    def get_comments(self, toid: int | None = None, **kwargs: Any) -> list[Comment]:
        """Implements API methods `users/{ids}/comments` and `users/{ids}/comments/{toid}`."""
        if toid is not None:
            url = f'users/{self.account_id}/comments/{toid}'
        else:
            url = f'users/{self.account_id}/comments'
        return self._get_call(url, Comment, **kwargs)

    def get_privileges(self, **kwargs: Any) -> list[Privilege]:
        return self._get_call(f'users/{self.account_id}/privileges', Privilege, **kwargs)

    def get_questions(self, **kwargs: Any) -> list[Question]:
        return self._get_call(f'users/{self.account_id}/questions', Question, **kwargs)
