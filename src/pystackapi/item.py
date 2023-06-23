from collections.abc import Iterator
from typing import Any


class Item:
    """Implements concrete item of API response."""
    def __init__(self, data: dict[Any, Any]) -> None:
        self.__data = data

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, dict):
            return self.__data == other
        elif isinstance(other, self.__class__):
            return self.__data == other.__data
        else:
            return NotImplemented

    def __repr__(self) -> str:
        return f'<Item with {len(self.__data)} key{"" if len(self.__data) == 1 else "s"}>'

    def __iter__(self) -> Iterator[tuple[Any, Any]]:
        return ((k, v) for k, v in self.__data.items())

    def __getattr__(self, name: str) -> Any:
        try:
            return getattr(self.__data, name)
        except AttributeError:
            return self.__data[name]

    def __getitem__(self, item: Any) -> Any:
        return self.__data[item]
