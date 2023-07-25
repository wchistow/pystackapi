"""Tests for method `Site.get_info`."""
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
def test_get_info_url() -> None:
    site.get_info()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/info/'
                                 '?site=stackoverflow')


@lest.register
def test_get_info_return_value() -> None:
    res = site.get_info()

    lest.assert_eq(res, Item({'id': 1}))
