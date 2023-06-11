from typing import Any

from .base import BaseModel, SiteT
from .answer import Answer
from .comment import Comment


class Question(BaseModel):
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)

    def get_answers(self, **kwargs: Any) -> list[Answer]:
        response = self._client.call(f'questions/{self.question_id}/answers', **kwargs)
        return [Answer(self._client, dict(data)) for data in response]

    def get_comments(self, **kwargs: Any) -> list[Comment]:
        response = self._client.call(f'questions/{self.question_id}/comments', **kwargs)
        return [Comment(self._client, dict(data)) for data in response]
