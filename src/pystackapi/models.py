from typing import Any, Protocol, TypeVar

from .response import Response


# Cannot import class `.site.Site` because of circular import.
class _Site(Protocol):
    def call(self, query: str, **kwargs: dict[str, Any]) -> Response: ...


_SiteT = TypeVar('_SiteT', bound=_Site)


class BaseModel:
    def __init__(self, client: _SiteT, data: dict[Any, Any]) -> None:
        self._data = data
        self._client = client

    def __getattr__(self, name: str) -> Any:
        return self._data[name]

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f'<{cls_name} model>'


class User(BaseModel):
    def __init__(self, client: _SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)

    def get_answers(self, **kwargs: Any) -> list['Answer']:
        response = self._client.call(f'users/{self.account_id}/answers', **kwargs)
        return [Answer(self._client, dict(data)) for data in response]

    def get_badges(self, **kwargs: Any) -> list['Badge']:
        response = self._client.call(f'users/{self.account_id}/badges', **kwargs)
        return [Badge(self._client, dict(data)) for data in response]


class Question(BaseModel):
    def __init__(self, client: _SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)

    def get_answers(self, **kwargs: Any) -> list['Answer']:
        response = self._client.call(f'questions/{self.question_id}/answers', **kwargs)
        return [Answer(self._client, dict(data)) for data in response]

    def get_comments(self, **kwargs: Any) -> list['Comment']:
        response = self._client.call(f'questions/{self.question_id}/comments', **kwargs)
        return [Comment(self._client, dict(data)) for data in response]


class Answer(BaseModel):
    def __init__(self, client: _SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)


class Comment(BaseModel):
    def __init__(self, client: _SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)


class Badge(BaseModel):
    def __init__(self, client: _SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)
