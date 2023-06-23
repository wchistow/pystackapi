"""Tests for class `Response`."""
import lest

from pystackapi.response import Response


@lest.register
def test_init() -> None:
    response = Response({'items': [], 'info': {'api_v': '2.3'}})

    lest.assert_eq(response.response_info, {'info': {'api_v': '2.3'}})
    lest.assert_eq(response._Response__items, [])


@lest.register
def test_iter() -> None:
    response = Response({'items': [{'id': 1}, {'id': 2}]})
    items = list(response)
    
    lest.assert_eq(len(items), 2)
    lest.assert_eq(items[0], {'id': 1})
    lest.assert_eq(items[1], {'id': 2})


@lest.register
def test_repr_with_one_item() -> None:
    response = Response({'items': [{'id': 1}]})
    
    lest.assert_eq(repr(response), '<Response object with 1 item>')


@lest.register
def test_repr_with_multy_items() -> None:
    response = Response({'items': [{'id': 1}, {'id': 2}]})

    lest.assert_eq(repr(response), '<Response object with 2 items>')


@lest.register
def test_getitem() -> None:
    response = Response({'items': [{'id': 1}]})
    
    lest.assert_eq(response[0], {'id': 1})
