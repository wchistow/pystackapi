"""Tests for method `Site.add_question`."""
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
def test_add_question_url() -> None:
    site.add_question(title='This is a test question.', body='This is a test question\'s body.',
                      tags=['testing', 'api'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'questions/add')
    lest.assert_eq(requests.data, {'site': 'stackoverflow', 'access_token': 'someaccesstoken',
                                   'key': 'someappkey', 'title': 'This is a test question.',
                                   'body': 'This is a test question\'s body.', 'tags': 'testing;api'
                                   }
                   )


@lest.register
def test_add_question_return_value() -> None:
    res = site.add_question(title='This is a test question.',
                            body='This is a test question\'s body.', tags=['testing', 'api'])

    lest.assert_eq(res, Item({'id': 1}))