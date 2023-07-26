"""Tests for `Site.get_suggested_edits` and `Site.get_suggested_edits_on_posts`."""
import lest

from pystackapi import site as site_m
from pystackapi.item import Item

from . import API_VERSION, requests

site_m.__dict__['requests'] = requests
site = site_m.Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


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
