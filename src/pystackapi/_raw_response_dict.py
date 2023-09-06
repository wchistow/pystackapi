from typing import TypedDict


class RawResponseDict(TypedDict):
    """Type of API response (returns by method `Site.get`)."""
    items: list[dict]
    has_more: bool
    quota_max: int
    quota_remaining: int
