"""Tests for `Site.get_collectives` and `Site.get_collective`."""
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
def test_get_collectives_without_slugs_url() -> None:
    site.get_collectives()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/collectives/'
                                 f'?site=stackoverflow')


@lest.register
def test_get_collectives_with_slugs_url() -> None:
    site.get_collectives(['co1', 'co2'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/collectives/co1;co2'
                                 f'?site=stackoverflow')


@lest.register
def test_get_collectives_return_value() -> None:
    res = site.get_collectives()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_collective_url() -> None:
    site.get_collective('co1')

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/collectives/co1'
                                 f'?site=stackoverflow')


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
