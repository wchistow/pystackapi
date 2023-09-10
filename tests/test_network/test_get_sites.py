"""Tests for methods `Network.create_filter` and `Network.get_filters`."""
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


@lest.register
def test_get_sites_url() -> None:
    network.get_sites()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/sites')


@lest.register
def test_get_sites_return_value() -> None:
    res = network.get_sites()

    lest.assert_eq(res, [Item({'id': 1})])
