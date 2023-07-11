"""Tests for `Site.get_collectives` and `Site.get_collective`."""
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
def test_get_collectives_without_slugs() -> None:
    site.get_collectives()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/collectives/?site=stackoverflow')


@lest.register
def test_get_collectives_with_slugs() -> None:
    site.get_collectives(['co1', 'co2'])

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/collectives/co1;co2?site=stackoverflow')


@lest.register
def test_return_value_of_get_collectives() -> None:
    res = site.get_collectives()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_collective() -> None:
    site.get_collective('co1')

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/collectives/co1?site=stackoverflow')


@lest.register
def test_return_value_of_get_collective() -> None:
    res = site.get_collective('co1')

    lest.assert_eq(res, Item({'id': 1}))
