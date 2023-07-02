"""Tests for class `Item`."""
import lest

from pystackapi.item import Item

item = Item({'id': 1})


@lest.register
def test_getattr() -> None:
    lest.assert_eq(item.id, 1)
