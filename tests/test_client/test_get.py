"""Tests for method `Site.get`."""
import lest

from pystackapi import site as site_m
from pystackapi.errors import HttpError
from pystackapi.item import Item

from mocks import RequestsMock

from . import requests

site_m.__dict__['requests'] = requests
site = site_m.Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


@lest.register
def test_simple_get() -> None:
    site.get('ghgh/')

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/ghgh/?site=stackoverflow')


@lest.register
def test_get_with_kwargs() -> None:
    site.get('ghgh/', arg1='hello')

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/ghgh/?site=stackoverflow&arg1=hello')


@lest.register
def test_get_with_access_token() -> None:
    l_site = site_m.Site('stackoverflow', access_token='someaccesstoken')
    l_site.get('ghgh/')

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/ghgh/?site=stackoverflow'
                   '&access_token=someaccesstoken')


@lest.register
def test_get_with_app_key() -> None:
    l_site = site_m.Site('stackoverflow', app_key='someappkey')
    l_site.get('ghgh/')

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/ghgh/?site=stackoverflow&key=someappkey')


@lest.register
def test_handling_error() -> None:
    l_requests = RequestsMock(status_code=400)

    site_m.__dict__['requests'] = l_requests
    l_site = site_m.Site('stackoverflow')

    with lest.assert_raises(HttpError):
        l_site.get('ghgh/')

    site_m.__dict__['requests'] = requests  # reset


@lest.register
def test_return_value_of_get() -> None:
    res = site.get('ghgh/')

    expected_result = {
        'items': [
            Item({'id': 1})
        ]
    }

    lest.assert_eq(res, expected_result)