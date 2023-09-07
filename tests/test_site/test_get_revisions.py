"""Tests for `Site.get_revisions` and `Site.get_revisions_on_posts`."""
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


# ---- tests for `Site.get_revisions` ----


@lest.register
def test_get_revisions_url() -> None:
    site.get_revisions([1])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/revisions/1'
                                 '?site=stackoverflow')


@lest.register
def test_get_revisions_return_value() -> None:
    res = site.get_revisions([1])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_revisions_on_posts` ----


@lest.register
def test_get_revisions_on_posts_url() -> None:
    site.get_revisions_on_posts([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/posts/1;2/revisions'
                                 '?site=stackoverflow')


@lest.register
def test_get_revisions_on_posts_return_value() -> None:
    res = site.get_revisions_on_posts([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])
