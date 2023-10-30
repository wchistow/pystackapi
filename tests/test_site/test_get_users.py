"""
Tests for `Site.get_users`, `Site.get_user`,
`Site.get_users_on_collectives`, `Site.get_moderators`,
`Site.get_elected_moderators` and `Site.get_me`.
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


# ---- tests for `Site.get_users` ----


@lest.register
def test_get_users_without_ids_url() -> None:
    site.get_users()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/users/'
                                 '?site=stackoverflow')


@lest.register
def test_get_users_with_ids_url() -> None:
    site.get_users([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/users/1;2'
                                 '?site=stackoverflow')


@lest.register
def test_get_users_return_value() -> None:
    res = site.get_users()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_user` ----


@lest.register
def test_get_user_url() -> None:
    site.get_user(1)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/users/1'
                                 '?site=stackoverflow')


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


# ---- tests for `Site.get_users_on_collectives` ----


@lest.register
def test_get_users_on_collectives_url() -> None:
    site.get_users_on_collectives(['co1', 'co2'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/collectives/co1;co2/users?site=stackoverflow')


@lest.register
def test_get_users_on_collectives_return_value() -> None:
    res = site.get_users_on_collectives(['co1', 'co2'])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_moderators` ----


@lest.register
def test_get_moderators_url() -> None:
    site.get_moderators()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/users/moderators?site=stackoverflow')


@lest.register
def test_get_moderators_return_value() -> None:
    res = site.get_moderators()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_elected_moderators` ----


@lest.register
def test_get_elected_moderators_url() -> None:
    site.get_elected_moderators()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/users/moderators/elected?site=stackoverflow')


@lest.register
def test_get_elected_moderators_return_value() -> None:
    res = site.get_elected_moderators()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_me` ----

@lest.register
def test_get_me_url() -> None:
    site.access_token = 'someaccesstoken'
    site.app_key = 'someappkey'
    site.get_me()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/me'
                                 '?site=stackoverflow&access_token=someaccesstoken&key=someappkey')

    # reset
    site.access_token = None
    site.app_key = None


@lest.register
def test_get_me_return_value() -> None:
    site.access_token = 'someaccesstoken'
    site.app_key = 'someappkey'
    res = site.get_me()

    lest.assert_eq(res, Item({'id': 1}))

    # reset
    site.access_token = None
    site.app_key = None


@lest.register
def test_get_me_without_access_token_and_app_key() -> None:
    with lest.assert_raises(AccessTokenOrAppKeyRequired):
        site.get_me()
