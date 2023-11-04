"""
Tests for
`Site.get_users_reputation`, `Site.get_users_reputation_history` and
`Site.get_my_full_reputation_history`.
"""
import lest

from pystackapi import _base_client as client_m
from pystackapi import Site
from pystackapi.item import Item
from pystackapi.errors import AccessTokenOrAppKeyRequired

from main import API_VERSION, requests

client_m.__dict__['requests'] = requests
site = Site('stackoverflow')


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


# ---- tests for `Site.get_my_full_reputation_history` ----


@lest.register
def test_get_my_full_reputation_history_url() -> None:
    site.access_token = 'someaccesstoken'
    site.app_key = 'someappkey'
    site.get_my_full_reputation_history()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'me/reputation-history/full'
                                 '?site=stackoverflow&access_token=someaccesstoken&key=someappkey')

    # reset
    site.access_token = None
    site.app_key = None


@lest.register
def test_get_my_full_reputation_history_return_value() -> None:
    site.access_token = 'someaccesstoken'
    site.app_key = 'someappkey'
    res = site.get_my_full_reputation_history()

    lest.assert_eq(res, [Item({'id': 1})])

    # reset
    site.access_token = None
    site.app_key = None


@lest.register
def test_get_my_unread_inbox_without_access_token_and_app_key() -> None:
    with lest.assert_raises(AccessTokenOrAppKeyRequired):
        site.get_my_full_reputation_history()
