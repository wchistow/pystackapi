"""Tests for method `Site.add_answer`."""
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


@lest.register
def test_add_answer_url() -> None:
    site.add_answer(1, 'This is a test answer.')

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'questions/1/answers/add')
    lest.assert_eq(requests.data, {'site': 'stackoverflow', 'access_token': 'someaccesstoken',
                                   'key': 'someappkey', 'body': 'This is a test answer.'}
                   )


@lest.register
def test_add_answer_return_value() -> None:
    res = site.add_answer(1, 'This is a test answer.')

    lest.assert_eq(res, Item({'id': 1}))
