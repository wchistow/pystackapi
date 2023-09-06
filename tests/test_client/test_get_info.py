"""Tests for method `Site.get_info`."""
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


@lest.register
def test_get_info_url() -> None:
    site.get_info()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/info?site=stackoverflow')


@lest.register
def test_get_info_return_value() -> None:
    res = site.get_info()

    lest.assert_eq(res, Item({'id': 1}))
