"""Tests for method `Site.get`."""
import lest

from pystackapi import _base_client as client_m
from pystackapi import Site

from main import API_VERSION, requests

client_m.__dict__['requests'] = requests
site = Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


@lest.register
def test_get_with_access_token_url() -> None:
    l_site = Site('stackoverflow', access_token='someaccesstoken')
    l_site.get('ghgh/')

    lest.assert_eq(requests.url,
                   f'https://api.stackexchange.com/{API_VERSION}/ghgh/?site=stackoverflow'
                   '&access_token=someaccesstoken')


@lest.register
def test_get_with_app_key_url() -> None:
    l_site = Site('stackoverflow', app_key='someappkey')
    l_site.get('ghgh/')

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/ghgh/'
                                 '?site=stackoverflow&key=someappkey')


@lest.register
def test_get_return_value() -> None:
    res = site.get('ghgh/')

    expected_result = {
        'items': [
            {'id': 1}
        ]
    }

    lest.assert_eq(res, expected_result)
