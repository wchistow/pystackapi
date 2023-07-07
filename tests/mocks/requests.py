"""Mock that replace the `requests` library."""
from typing import Any


class RequestsMock:
    def __init__(self, return_items: list[Any] | None = None, status_code: int = 200) -> None:
        """
        :param return_items: what is in the `'items'` key of response
        :param status_code: what is status code of response
        """
        self.return_items = return_items or []

        self.url: str | None = None
        self.status_code = status_code

    def get(self, url: str) -> 'ResponseMock':
        self.url = url
        return ResponseMock(self.status_code, {'items': self.return_items})

    def reset(self) -> None:
        self.url = None


class ResponseMock:
    def __init__(self, status_code: int, data: dict) -> None:
        self.status_code = status_code
        self.data = data

    def json(self) -> dict:
        return self.data
