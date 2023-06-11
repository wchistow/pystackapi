from typing import Any, Protocol, TypeVar

from ..response import Response


# Cannot import class `.site.Site` because of circular import.
class _Site(Protocol):
    def call(self, query: str, **kwargs: dict[str, Any]) -> Response: ...


SiteT = TypeVar('SiteT', bound=_Site)


class BaseModel:
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        self._data = data
        self._client = client

    def __getattr__(self, name: str) -> Any:
        return self._data[name]

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f'<{cls_name} model>'
