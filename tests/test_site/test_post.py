"""Tests for method `Site.post`."""
import lest

from pystackapi import _base_client as client_m
from pystackapi import Site
from pystackapi.errors import AccessTokenOrAppKeyRequired

from main import API_VERSION, requests

client_m.__dict__['requests'] = requests
site = Site('stackoverflow', access_token='someaccesstoken', app_key='someappkey')


@lest.setup
def reset_requests() -> None:
    requests.reset()


@lest.register
def test_simple_post() -> None:
    site.post('ghgh/')

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/ghgh/')
    lest.assert_eq(requests.data, {'site': 'stackoverflow', 'access_token': 'someaccesstoken',
                                   'key': 'someappkey'}
                   )


@lest.register
def test_post_without_access_token_or_app_key() -> None:
    site.access_token = None

    with lest.assert_raises(AccessTokenOrAppKeyRequired):
        site.post('ghgh/')

    # reset
    site.access_token = 'someaccesstoken'


@lest.register
def test_post_return_value() -> None:
    res = site.post('ghgh/')

    expected_result = {
        'items': [
            {'id': 1}
        ]
    }

    lest.assert_eq(res, expected_result)
