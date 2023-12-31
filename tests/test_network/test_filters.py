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


# ---- tests for `Network.create_filter` ----


@lest.register
def test_create_filter_url() -> None:
    network.create_filter()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/filters/create')


@lest.register
def test_create_filter_return_value() -> None:
    res = network.create_filter()

    lest.assert_eq(res, Item({'id': 1}))


# ---- tests for `Network.get_filters` ----


@lest.register
def test_get_filters_url() -> None:
    network.get_filters(['filter1', 'filter2'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'filters/filter1;filter2')


@lest.register
def test_get_filters_return_value() -> None:
    res = network.get_filters(['filter1', 'filter2'])

    lest.assert_eq(res, [Item({'id': 1})])
