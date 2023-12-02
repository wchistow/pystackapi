"""Tests for methods `Site.add_*`."""
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


# ---- tests for method `Site.add_answer` ----


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


# ---- tests for method `Site.add_comment` ----


@lest.register
def test_add_comment_url() -> None:
    site.add_comment(1, 'This is a test comment.')

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'posts/1/comments/add')
    lest.assert_eq(requests.data, {'site': 'stackoverflow', 'access_token': 'someaccesstoken',
                                   'key': 'someappkey', 'body': 'This is a test comment.'}
                   )


@lest.register
def test_add_comment_return_value() -> None:
    res = site.add_comment(1, 'This is a test comment.')

    lest.assert_eq(res, Item({'id': 1}))


# ---- tests for method `Site.add_question` ----


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
    lest.assert_eq(res, Item({'id': 1}))
