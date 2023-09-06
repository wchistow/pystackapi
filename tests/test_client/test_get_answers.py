"""
Tests for `Site.get_answers`, `Site.get_answer`,
`Site.get_answers_on_collectives`, `Site.get_answers_on_questions` and
`Site.get_users_answers`.
"""
import lest

from pystackapi import _base_client as client_m
from pystackapi import Site
from pystackapi.item import Item

from . import API_VERSION, requests

client_m.__dict__['requests'] = requests
site = Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


# ---- tests for `Site.get_answers` ----


@lest.register
def test_get_answers_without_ids_url() -> None:
    site.get_answers()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/answers/'
                                 '?site=stackoverflow')


@lest.register
def test_get_answers_with_ids_url() -> None:
    site.get_answers([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/answers/1;2'
                                 '?site=stackoverflow')


@lest.register
def test_get_answers_return_value() -> None:
    res = site.get_answers()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_answer` ----


@lest.register
def test_get_answer_url() -> None:
    site.get_answer(1)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/answers/1'
                                 '?site=stackoverflow')


@lest.register
def test_get_answer_return_value() -> None:
    res = site.get_answer(1)

    lest.assert_eq(res, Item({'id': 1}))


@lest.register
def test_get_answer_with_no_data() -> None:
    requests.no_data = [f'https://api.stackexchange.com/{API_VERSION}/answers/1?site=stackoverflow']

    res = site.get_answer(1)

    lest.assert_true(res is None)

    requests.no_data = []


# ---- tests for `Site.get_answers_on_collectives` ----


@lest.register
def test_get_answers_on_collectives_url() -> None:
    site.get_answers_on_collectives(['co1', 'co2'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/collectives/co1;co2/answers?site=stackoverflow')


@lest.register
def test_get_answers_on_collectives_return_value() -> None:
    res = site.get_answers_on_collectives(['co1', 'co2'])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_answers_on_questions` ----


@lest.register
def test_get_answers_on_questions_url() -> None:
    site.get_answers_on_questions([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'questions/1;2/answers?site=stackoverflow')


@lest.register
def test_get_answers_on_questions_return_value() -> None:
    res = site.get_answers_on_questions([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_users_answers` ----


@lest.register
def test_get_users_answers_url() -> None:
    site.get_users_answers([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'users/1;2/answers?site=stackoverflow')


@lest.register
def test_get_users_answers_return_value() -> None:
    res = site.get_users_answers([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])
