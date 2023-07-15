"""Tests for `Site.get_privileges`."""
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
def test_get_privileges_url() -> None:
    site.get_privileges()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/privileges/?site=stackoverflow')


@lest.register
def test_get_privileges_return_value() -> None:
    res = site.get_privileges()

    lest.assert_eq(res, [Item({'id': 1})])
