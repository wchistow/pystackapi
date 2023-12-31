"""Tests for `Site.get_articles` and `Site.get_article`."""
import lest

from pystackapi import _base_client as client_m
from pystackapi import Site
from pystackapi.item import Item

from main import API_VERSION, requests

client_m.__dict__['requests'] = requests
site = Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


# ---- tests for `Site.get_articles` ----


@lest.register
def test_get_articles_without_ids_url() -> None:
    site.get_articles()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/articles/'
                                 '?site=stackoverflow')


@lest.register
def test_get_articles_with_ids_url() -> None:
    site.get_articles([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/articles/1;2'
                                 '?site=stackoverflow')


@lest.register
def test_get_articles_return_value() -> None:
    res = site.get_articles()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_article` ----


@lest.register
def test_get_article_url() -> None:
    site.get_article(1)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/articles/1'
                                 '?site=stackoverflow')


@lest.register
def test_get_article_return_value() -> None:
    res = site.get_article(1)

    lest.assert_eq(res, Item({'id': 1}))


@lest.register
def test_get_article_with_no_data() -> None:
    requests.no_data = [
        f'https://api.stackexchange.com/{API_VERSION}/articles/1?site=stackoverflow'
    ]

    res = site.get_article(1)

    lest.assert_true(res is None)

    requests.no_data = []
