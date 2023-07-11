"""Tests for method `Site.get_info`."""
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
def test_get_info() -> None:
    site.get_info()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/info/?site=stackoverflow')


@lest.register
def test_return_value_of_get_info() -> None:
    res = site.get_info()

    lest.assert_eq(res, Item({'id': 1}))