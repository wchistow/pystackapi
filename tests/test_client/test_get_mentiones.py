"""Tests for `Site.get_users_mentions`."""
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
def test_get_users_mentions_url() -> None:
    site.get_users_mentions([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'users/1;2/mentioned?site=stackoverflow')


@lest.register
def test_get_users_mentions_return_value() -> None:
    res = site.get_users_mentions([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])
