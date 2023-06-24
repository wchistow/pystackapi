"""Tests for class `Item`."""
import lest

from pystackapi.item import Item

item = Item({'id': 1})


@lest.register
def test_init() -> None:
    lest.assert_eq(item._Item__data, {'id': 1})


@lest.register
def test_eq_with_dict() -> None:
    lest.assert_true(item == {'id': 1})


@lest.register
def test_eq_with_item() -> None:
    lest.assert_true(item == Item({'id': 1}))


@lest.register
def test_repr_with_one() -> None:
    lest.assert_eq(repr(item), '<Item with 1 key>')


@lest.register
def test_repr_with_many() -> None:
    item_with_many_keys = Item({'id': 1, 'title': 'some title'})

    lest.assert_eq(repr(item_with_many_keys), '<Item with 2 keys>')


@lest.register
def test_iter() -> None:
    item_with_many_keys = Item({'id': 1, 'title': 'some title'})
    
    lest.assert_eq(list(item_with_many_keys), [('id', 1), ('title', 'some title')])


@lest.register
def test_getattr() -> None:
    lest.assert_eq(item.id, 1)


@lest.register
def test_getitem() -> None:
    lest.assert_eq(item['id'], 1)
