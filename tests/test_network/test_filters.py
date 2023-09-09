"""Tests for methods `Network.create_filter`."""
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
def test_create_filter_url() -> None:
    network.create_filter()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/filters/create')


@lest.register
def test_create_filter_return_value() -> None:
    res = network.create_filter()

    lest.assert_eq(res, Item({'id': 1}))
