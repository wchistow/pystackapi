"""Tests for method `BaseClient._get`."""
import lest

from pystackapi import _base_client as client_m
from pystackapi._base_client import BaseClient
from pystackapi.errors import HttpError

from mocks import RequestsMock

from main import requests

client_m.__dict__['requests'] = requests
base_client = BaseClient()


@lest.setup
def reset_requests() -> None:
    requests.reset()


@lest.register
def test_simple_get_url() -> None:
    base_client._get('http://somesite.org/somepage.html', {})

    lest.assert_eq(requests.url, 'http://somesite.org/somepage.html')


@lest.register
def test_get_with_one_arg_url() -> None:
    base_client._get('http://somesite.org/somepage.html', {'arg1': 'hello'})

    lest.assert_eq(requests.url, 'http://somesite.org/somepage.html?arg1=hello')


@lest.register
def test_get_with_many_args_url() -> None:
    base_client._get('http://somesite.org/somepage.html', {'arg1': 'a', 'arg2': 'b', 'arg3': 'c'})

    lest.assert_eq(requests.url, 'http://somesite.org/somepage.html?arg1=a&arg2=b&arg3=c')


@lest.register
def test_handling_error() -> None:
    l_requests = RequestsMock(status_code=400)

    client_m.__dict__['requests'] = l_requests
    l_base_client = BaseClient()

    with lest.assert_raises(HttpError):
        l_base_client._get('http://somesite.org/somepage.html', {})

    client_m.__dict__['requests'] = requests  # reset


@lest.register
def test_get_return_value() -> None:
    res = base_client._get('http://somesite.org/somepage.html', {})

    lest.assert_eq(res, {'items': [{'id': 1}]})
