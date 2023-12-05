"""Tests for methods `Site.delete_*`."""
import lest

from pystackapi import _base_client as client_m
from pystackapi import Site
from pystackapi.item import Item

from main import API_VERSION, requests

client_m.__dict__['requests'] = requests
site = Site('stackoverflow', access_token='someaccesstoken', app_key='someappkey')


@lest.setup
def reset_requests() -> None:
    requests.reset()


# ---- tests for method `Site.delete_answer` ----


@lest.register
def test_delete_answer_url() -> None:
    site.delete_answer(1)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'answers/1/delete')
    lest.assert_eq(requests.data, {'site': 'stackoverflow', 'access_token': 'someaccesstoken',
                                   'key': 'someappkey'
                                   }
                   )


@lest.register
def test_delete_answer_return_value() -> None:
    res = site.delete_answer(1)

    lest.assert_eq(res, None)
