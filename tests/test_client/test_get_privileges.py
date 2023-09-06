"""Tests for `Site.get_privileges` and `Site.get_user_privileges`."""
import lest

from pystackapi import _base_client as client_m
from pystackapi import Site
from pystackapi.item import Item

from . import API_VERSION, requests

client_m.__dict__['requests'] = requests
site = Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


# ---- tests for `Site.get_privileges` ----


@lest.register
def test_get_privileges_url() -> None:
    site.get_privileges()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/privileges?site=stackoverflow')


@lest.register
def test_get_privileges_return_value() -> None:
    res = site.get_privileges()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_users_privileges` ----


@lest.register
def test_get_user_privileges_url() -> None:
    site.get_user_privileges(1)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'users/1/privileges?site=stackoverflow')


@lest.register
def test_get_user_privileges_return_value() -> None:
    res = site.get_user_privileges(1)

    lest.assert_eq(res, [Item({'id': 1})])
