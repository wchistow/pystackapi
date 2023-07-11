"""Tests for `Site.get_users` and `Site.get_user`."""
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
def test_get_users_without_ids() -> None:
    site.get_users()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/users/?site=stackoverflow')


@lest.register
def test_get_users_with_ids() -> None:
    site.get_users([1, 2])

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/users/1;2?site=stackoverflow')


@lest.register
def test_return_value_of_get_users() -> None:
    res = site.get_users()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_user() -> None:
    site.get_user(1)

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/users/1?site=stackoverflow')


@lest.register
def test_return_value_of_get_user() -> None:
    res = site.get_user(1)

    lest.assert_eq(res, Item({'id': 1}))
