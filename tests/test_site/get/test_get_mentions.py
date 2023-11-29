"""Tests for `Site.get_users_mentions`."""
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


@lest.register
def test_get_users_mentions_url() -> None:
    site.get_users_mentions([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'users/1;2/mentioned?site=stackoverflow')


@lest.register
def test_get_users_mentions_return_value() -> None:
    res = site.get_users_mentions([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])
