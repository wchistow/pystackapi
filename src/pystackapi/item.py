from collections import UserDict
from typing import Any


class Item(UserDict[str, Any]):
    """Useful class to discover JSON data."""
    def __getattr__(self, name: str) -> Any:
        return self.data[name]

    """Improved Readability for Item Data"""
    def __str__(self) -> str:
        out = []
        for attr in self.data:
            out.append(f'{attr}: {self.data[attr]}\n')
        return ''.join(out)
