"""Tests for `Site.get_users_reputation` and `Site.get_users_reputation_history`."""
import lest

from pystackapi import site as site_m
from pystackapi.item import Item

from . import API_VERSION, requests

site_m.__dict__['requests'] = requests
site = site_m.Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


# ---- tests for `Site.get_users_reputation` ----


@lest.register
def test_get_users_reputation_url() -> None:
    site.get_users_reputation([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 f'users/1;2/reputation?site=stackoverflow')


@lest.register
def test_get_users_reputation_return_value() -> None:
    res = site.get_users_reputation([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_users_reputation_history` ----


@lest.register
def test_get_users_reputation_history_url() -> None:
    site.get_users_reputation_history([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 f'users/1;2/reputation-history?site=stackoverflow')


@lest.register
def test_get_users_reputation_history_return_value() -> None:
    res = site.get_users_reputation_history([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])
