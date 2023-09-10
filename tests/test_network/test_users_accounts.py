"""
Tests for methods `Network.get_users_associated_accounts` and `Network.get_users_accounts_merges`.
"""
import lest

from pystackapi import _base_client as client_m
from pystackapi import Network
from pystackapi.item import Item

from main import API_VERSION, requests

client_m.__dict__['requests'] = requests
network = Network()


@lest.setup
def reset_requests() -> None:
    requests.reset()


# ---- tests for `Network.get_users_associated_accounts` ----


@lest.register
def test_get_users_associated_accounts_url() -> None:
    network.get_users_associated_accounts([1, 2])

    lest.assert_eq(requests.url,
                   f'https://api.stackexchange.com/{API_VERSION}/users/1;2/associated')


@lest.register
def test_get_users_associated_accounts_return_value() -> None:
    res = network.get_users_associated_accounts([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Network.get_users_accounts_merges` ----


@lest.register
def test_get_users_accounts_merges_url() -> None:
    network.get_users_accounts_merges([1, 2])

    lest.assert_eq(requests.url,
                   f'https://api.stackexchange.com/{API_VERSION}/users/1;2/merges')


@lest.register
def test_get_users_accounts_merges_return_value() -> None:
    res = network.get_users_accounts_merges([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])
