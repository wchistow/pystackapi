from typing import Any, Protocol, Type, TypeVar

from ..response import Response


# Cannot import class `.site.Site` because of circular import.
class _Site(Protocol):
    def call(self, query: str, **kwargs: dict[str, Any]) -> Response: ...


SiteT = TypeVar('SiteT', bound=_Site)
BaseModelT_co = TypeVar('BaseModelT_co', bound='BaseModel', covariant=True)


class BaseModel:
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        self._data = data
        self._client = client

    def _get_call(self, url: str, model: Type[BaseModelT_co], **kwargs: Any) -> list[BaseModelT_co]:
        response = self._client.call(url, **kwargs)
        return [model(self._client, dict(data)) for data in response]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseModel):
            return NotImplemented
        return self._data == other._data

    def __getattr__(self, name: str) -> Any:
        return self._data[name]

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f'<{cls_name} model>'
