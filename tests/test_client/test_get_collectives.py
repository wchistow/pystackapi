"""Tests for `Site.get_collectives` and `Site.get_collective`."""
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


# ---- tests for `Site.get_collectives` ----


@lest.register
def test_get_collectives_without_slugs_url() -> None:
    site.get_collectives()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/collectives/'
                                 '?site=stackoverflow')


@lest.register
def test_get_collectives_with_slugs_url() -> None:
    site.get_collectives(['co1', 'co2'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/collectives/co1;co2'
                                 '?site=stackoverflow')


@lest.register
def test_get_collectives_return_value() -> None:
    res = site.get_collectives()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_collective` ----


@lest.register
def test_get_collective_url() -> None:
    site.get_collective('co1')

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/collectives/co1'
                                 '?site=stackoverflow')


@lest.register
def test_get_collective_return_value() -> None:
    res = site.get_collective('co1')

    lest.assert_eq(res, Item({'id': 1}))


@lest.register
def test_get_collective_with_no_data() -> None:
    requests.no_data = [
        f'https://api.stackexchange.com/{API_VERSION}/collectives/co1?site=stackoverflow'
    ]

    res = site.get_collective('co1')

    lest.assert_true(res is None)

    requests.no_data = []
