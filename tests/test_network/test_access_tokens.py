"""Tests for methods `Network.invalidate_access_tokens` and `Network.get_access_tokens`."""
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
def test_invalidate_access_tokens_url() -> None:
    network.invalidate_access_tokens(['accesstoken1', 'accesstoken2'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'access-tokens/accesstoken1;accesstoken2/invalidate')


@lest.register
def test_invalidate_access_tokens_return_value() -> None:
    res = network.invalidate_access_tokens(['accesstoken1', 'accesstoken2'])

    lest.assert_eq(res, [Item({'id': 1})])
