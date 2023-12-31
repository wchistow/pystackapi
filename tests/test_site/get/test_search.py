"""Tests for `Site.search`, `Site.advanced_search` and `Site.get_similar`."""
import lest

from pystackapi import _base_client as client_m
from pystackapi import Site
from pystackapi.item import Item
from pystackapi.errors import BadArgumentsError

from main import API_VERSION, requests

client_m.__dict__['requests'] = requests
site = Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


# ---- tests for `Site.search`. ----


@lest.register
def test_search_url() -> None:
    site.search(tagged='python')

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/search?site=stackoverflow&tagged=python')


@lest.register
def test_search_raises_error() -> None:
    with lest.assert_raises(BadArgumentsError):
        site.search()


@lest.register
def test_search_return_value() -> None:
    res = site.search(tagged='python')

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.advanced_search`


@lest.register
def test_advanced_search_url() -> None:
    site.advanced_search()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/search/advanced?site=stackoverflow')


@lest.register
def test_advanced_search_return_value() -> None:
    res = site.advanced_search()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_similar` ----


@lest.register
def test_get_similar_url() -> None:
    site.get_similar('some_title')

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/similar?site=stackoverflow&title=some_title')


@lest.register
def test_get_similar_return_value() -> None:
    res = site.get_similar('some_title')

    lest.assert_eq(res, [Item({'id': 1})])
