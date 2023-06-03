from collections.abc import Iterator
from typing import Any

from .item import Item


class Response:
    """Implements result of API calling."""
    def __init__(self, data: dict) -> None:
        self.__items = list(map(Item, data['items']))
        self.response_info = {k: v for k, v in data.items() if k != 'items'}

    def __iter__(self) -> Iterator:
        return iter(self.__items)

    def __repr__(self) -> str:
        return f'<Response object with {len(self.__items)} ' \
               f'item{"" if len(self.__items) == 1 else "s"}>'

    def __getitem__(self, item: int) -> Any:
        return self.__items[item]
