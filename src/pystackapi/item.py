from collections import UserDict
from typing import Any


class Item(UserDict[str, Any]):
    """Useful class to discover JSON data."""
    def __getattr__(self, name: str) -> Any:
        return self.data[name]
