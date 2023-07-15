"""Tests for `Site.get_comments` and `Site.get_comment`."""
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
def test_get_comments_without_ids_url() -> None:
    site.get_comments()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/comments/?site=stackoverflow')


@lest.register
def test_get_comments_with_ids_url() -> None:
    site.get_comments([1, 2])

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/comments/1;2?site=stackoverflow')


@lest.register
def test_get_comments_return_value() -> None:
    res = site.get_comments()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_comment_url() -> None:
    site.get_comment(1)

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/comments/1?site=stackoverflow')


@lest.register
def test_get_comment_return_value() -> None:
    res = site.get_comment(1)

    lest.assert_eq(res, Item({'id': 1}))
