"""
Tests for `Site.get_suggested_edits`, `Site.get_suggested_edits_on_posts` and
`Site.get_users_suggested_edits`.
"""
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


# ---- tests for `Site.get_suggested_edits` ----


@lest.register
def test_get_suggested_edits_without_ids_url() -> None:
    site.get_suggested_edits()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/suggested-edits/'
                                 '?site=stackoverflow')


@lest.register
def test_get_suggested_edits_with_ids_url() -> None:
    site.get_suggested_edits([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/suggested-edits/1;2'
                                 '?site=stackoverflow')


@lest.register
def test_get_suggested_edits_return_value() -> None:
    res = site.get_suggested_edits()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_suggested_edits_on_posts` ----


@lest.register
def test_get_suggested_edits_on_posts_url() -> None:
    site.get_suggested_edits_on_posts([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 f'posts/1;2/suggested-edits?site=stackoverflow')


@lest.register
def test_get_suggested_edits_on_posts_return_value() -> None:
    res = site.get_suggested_edits_on_posts([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_users_suggested_edits` ----


@lest.register
def test_get_users_suggested_edits_url() -> None:
    site.get_users_suggested_edits([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 f'users/1;2/suggested-edits?site=stackoverflow')


@lest.register
def test_get_users_suggested_edits_return_value() -> None:
    res = site.get_users_suggested_edits([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])
