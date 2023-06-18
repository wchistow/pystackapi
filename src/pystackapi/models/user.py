from typing import Any

from .base import BaseModel, SiteT
from .answer import Answer
from .badge import Badge
from .comment import Comment
from .priviledge import Privilege
from .question import Question


class User(BaseModel):
    """Implements the user object - https://api.stackexchange.com/docs/types/user."""
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)

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
