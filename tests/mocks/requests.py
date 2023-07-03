"""Mock that replace the `requests` library."""
from typing import Any


class RequestsMock:
    def __init__(self, return_items: list[Any] | None = None) -> None:
        self.return_items = return_items or []

        self.url: str | None = None

    def get(self, url: str) -> 'ResponseMock':
        self.url = url
        return ResponseMock(200, {'items': self.return_items})

    def reset(self) -> None:
        self.url = None


class ResponseMock:
    def __init__(self, status_code: int, data: dict) -> None:
        self.status_code = status_code
        self.data = data

    def json(self) -> dict:
        return self.data
