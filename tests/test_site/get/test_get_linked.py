"""Tests for `Site.get_linked_in_articles` and `Site.get_linked_in_questions`."""
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


# ---- tests for `Site.get_linked_in_articles` ----


@lest.register
def test_get_linked_in_articles_url() -> None:
    site.get_linked_in_articles([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/articles/1;2/'
                                 'linked?site=stackoverflow')


@lest.register
def test_get_linked_in_articles_return_value() -> None:
    res = site.get_linked_in_articles([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_linked_in_questions` ----


@lest.register
def test_get_linked_in_questions_url() -> None:
    site.get_linked_in_questions([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/questions/1;2/'
                                 'linked?site=stackoverflow')


@lest.register
def test_get_linked_in_questions_return_value() -> None:
    res = site.get_linked_in_questions([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])
