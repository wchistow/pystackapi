from typing import Any

from .base import BaseModel, SiteT
from .comment import Comment


class Answer(BaseModel):
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)

    def get_comments(self, **kwargs: Any) -> list[Comment]:
        return self._get_call(f'answers/{self.answer_id}/comments', Comment, **kwargs)
