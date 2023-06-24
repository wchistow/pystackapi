from typing import Any

from pystackapi.response import Response


class ClientPatch:
    """Implements client for tests."""
    def __init__(self, return_items: list[Any] | None = None) -> None:
        self.query: str | None = None
        self.kwargs: dict[str, Any] | None = None
        self.return_items = return_items or []

    def call(self, query: str, **kwargs: Any) -> Response:
        self.query = query
        self.kwargs = kwargs
        
        return Response({'items': self.return_items})  # "empty" response
