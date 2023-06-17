from typing import Any

from .base import BaseModel, SiteT
from .answer import Answer
from .comment import Comment


class Question(BaseModel):
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)

    def get_answers(self, **kwargs: Any) -> list[Answer]:
        return self._get_call(f'questions/{self.question_id}/answers', Answer, **kwargs)

    def get_comments(self, **kwargs: Any) -> list[Comment]:
        return self._get_call(f'questions/{self.question_id}/comments', Comment, **kwargs)
