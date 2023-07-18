"""Tests for `Site.get_posts` and `Site.get_post`."""
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
def test_get_posts_without_ids_url() -> None:
    site.get_posts()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/posts/'
                                 '?site=stackoverflow')


@lest.register
def test_get_posts_with_ids_url() -> None:
    site.get_posts([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/posts/1;2'
                                 '?site=stackoverflow')


@lest.register
def test_get_posts_return_value() -> None:
    res = site.get_posts([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_post_url() -> None:
    site.get_post(1)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/posts/1'
                                 '?site=stackoverflow')


@lest.register
def test_get_post_return_value() -> None:
    res = site.get_post(1)

    lest.assert_eq(res, Item({'id': 1}))


@lest.register
def test_get_post_with_no_data() -> None:
    requests.no_data = [
        f'https://api.stackexchange.com/{API_VERSION}/posts/1?site=stackoverflow'
    ]

    res = site.get_post(1)

    lest.assert_true(res is None)

    requests.no_data = []
