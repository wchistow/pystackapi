from typing import Any

from pystackapi.item import Item


class ClientMock:
    """Implements client for tests."""
    def __init__(self, return_items: list | None = None) -> None:
        self.query: str | None = None
        self.kwargs: dict[str, Any] | None = None
        self.return_items = return_items or []

    def call(self, query: str, **kwargs: Any) -> dict:
        self.query = query
        self.kwargs = kwargs
        
        return {'items': [Item(item) for item in self.return_items]}
