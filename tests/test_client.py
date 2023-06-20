from typing import Any

from pystackapi.response import Response


class TestClient:
    """Implements client for tests."""
    def __init__(self) -> None:
        self.query: str | None = None
        self.kwargs: dict[str, Any] | None = None

    def call(self, query: str, **kwargs: Any) -> Response:
        self.query = query
        self.kwargs = kwargs
        
        return Response({'items': []})  # "empty " response
