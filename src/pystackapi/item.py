from collections.abc import Iterator
from typing import Any


class Item:
    """Implements concrete item of API response."""
    def __init__(self, data: dict) -> None:
        self.__data = data

    def __repr__(self) -> str:
        return f'<Item with {len(self.__data)} key{"" if len(self.__items) == 1 else "s"}>'

    def __iter__(self) -> Iterator:
        return ((k, v) for k, v in self.__data.items())

    def __getattr__(self, name: str) -> Any:
        try:
            return getattr(self.__data, name)
        except AttributeError:
            return self.__data[name]

    def __getitem__(self, item: Any) -> Any:
        return self.__data[item]
