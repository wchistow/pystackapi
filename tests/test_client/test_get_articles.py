"""Tests for `Site.get_articles` and `Site.get_article`."""
import lest

from pystackapi import site as site_m
from pystackapi.item import Item

from . import requests

site_m.__dict__['requests'] = requests
site = site_m.Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


@lest.register
def test_get_articles_without_ids() -> None:
    site.get_articles()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/articles/?site=stackoverflow')


@lest.register
def test_get_articles_with_ids() -> None:
    site.get_articles([1, 2])

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/articles/1;2?site=stackoverflow')


@lest.register
def test_return_value_of_get_articles() -> None:
    res = site.get_articles()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_article() -> None:
    site.get_article(1)

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/articles/1?site=stackoverflow')


@lest.register
def test_return_value_of_get_article() -> None:
    res = site.get_article(1)

    lest.assert_eq(res, Item({'id': 1}))
