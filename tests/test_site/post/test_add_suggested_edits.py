"""Tests for methods `Site.add_*_suggested_edit`."""
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


# ---- tests for method `Site.add_answers_suggested_edit` ----


@lest.register
def test_add_answers_suggested_edit_url() -> None:
    site.add_answers_suggested_edit(1, 'This is new body', 'test edit')

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'answers/1/suggested-edit/add')
    lest.assert_eq(requests.data, {'site': 'stackoverflow', 'access_token': 'someaccesstoken',
                                   'key': 'someappkey', 'body': 'This is new body',
                                   'comment': 'test edit'
                                   }
                   )


@lest.register
def test_add_answers_suggested_edit_return_value() -> None:
    res = site.add_answers_suggested_edit(1, 'This is new body', 'test edit')

    lest.assert_eq(res, Item({'id': 1}))


# ---- tests for method `Site.add_questions_suggested_edit` ----


@lest.register
def test_add_questions_suggested_edit_url() -> None:
    site.add_questions_suggested_edit(1, 'This is new title', 'This is new body',
                                      ['old-tag', 'new-tag'], 'test edit')

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'questions/1/suggested-edit/add')
    lest.assert_eq(requests.data, {'site': 'stackoverflow', 'access_token': 'someaccesstoken',
                                   'key': 'someappkey', 'title': 'This is new title',
                                   'body': 'This is new body', 'tags': 'old-tag;new-tag',
                                   'comment': 'test edit'
                                   }
                   )


@lest.register
def test_add_answers_suggested_edit_return_value() -> None:
    res = site.add_questions_suggested_edit(1, 'This is new title', 'This is new body',
                                      ['old-tag', 'new-tag'], 'test edit')

    lest.assert_eq(res, Item({'id': 1}))
