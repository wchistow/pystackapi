"""Tests for `Site.get_users` and `Site.get_user`."""
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
def test_get_users_without_ids_url() -> None:
    site.get_users()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/users/'
                                 f'?site=stackoverflow')


@lest.register
def test_get_users_with_ids_url() -> None:
    site.get_users([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/users/1;2'
                                 f'?site=stackoverflow')


@lest.register
def test_get_users_return_value() -> None:
    res = site.get_users()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_user_url() -> None:
    site.get_user(1)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/users/1'
                                 f'?site=stackoverflow')


@lest.register
def test_get_user_return_value() -> None:
    res = site.get_user(1)

    lest.assert_eq(res, Item({'id': 1}))


@lest.register
def test_get_user_with_no_data() -> None:
    requests.no_data = [
        f'https://api.stackexchange.com/{API_VERSION}/users/1?site=stackoverflow'
    ]

    res = site.get_user(1)

    lest.assert_true(res is None)

    requests.no_data = []
