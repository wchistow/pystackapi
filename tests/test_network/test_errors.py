"""Tests for methods `Network.get_errors` and `simulate_error`."""
import lest

from pystackapi import _base_client as client_m
from pystackapi import Network
from pystackapi.item import Item
from pystackapi.errors import HttpError

from main import API_VERSION, requests

from mocks import RequestsMock

client_m.__dict__['requests'] = requests
network = Network()


@lest.setup
def reset_requests() -> None:
    requests.reset()


# ---- tests for `Network.get_errors` ----


@lest.register
def test_get_errors_without_id_url() -> None:
    network.get_errors()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/errors')


@lest.register
def test_get_errors_without_id_return_value() -> None:
    res = network.get_errors()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- test for `Network.simulate_error` ----


@lest.register
def test_simulate_error() -> None:
    l_requests = RequestsMock(status_code=404)

    client_m.__dict__['requests'] = l_requests
    l_network = Network()

    with lest.assert_raises(HttpError):
        l_network.simulate_error(404)

    client_m.__dict__['requests'] = requests  # reset
