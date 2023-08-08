"""
Tests for
`Site.get_questions`, `Site.get_question`,
`Site.get_questions_on_answers`, `Site.get_questions_on_collectives`,
`Site.get_bountied_questions`, `Site.get_questions_with_no_answers` and
`Site.get_unanswered_questions`.
"""
import lest

from pystackapi import site as site_m
from pystackapi.item import Item

from . import API_VERSION, requests

site_m.__dict__['requests'] = requests
site = site_m.Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


@lest.register
def test_get_questions_without_ids_url() -> None:
    site.get_questions()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/questions/'
                                 '?site=stackoverflow')


@lest.register
def test_get_questions_with_ids_url() -> None:
    site.get_questions([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/questions/1;2'
                                 '?site=stackoverflow')


@lest.register
def test_get_questions_return_value() -> None:
    res = site.get_questions()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_question_url() -> None:
    site.get_question(1)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/questions/1'
                                 '?site=stackoverflow')


@lest.register
def test_get_question_return_value() -> None:
    res = site.get_question(1)

    lest.assert_eq(res, Item({'id': 1}))


@lest.register
def test_get_question_with_no_data() -> None:
    requests.no_data = [
        f'https://api.stackexchange.com/{API_VERSION}/questions/1?site=stackoverflow'
    ]

    res = site.get_question(1)

    lest.assert_true(res is None)

    requests.no_data = []


# ---- tests for `Site.get_questions_on_answers` ----


@lest.register
def test_get_questions_on_answers_url() -> None:
    site.get_questions_on_answers([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/answers/1;2/questions?site=stackoverflow')


@lest.register
def test_get_questions_on_answers_return_value() -> None:
    res = site.get_questions_on_answers([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_questions_on_collectives` ----


@lest.register
def test_get_questions_on_collectives_url() -> None:
    site.get_questions_on_collectives(['co1', 'co2'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/collectives/co1;co2/questions?site=stackoverflow')


@lest.register
def test_get_questions_on_collectives_return_value() -> None:
    res = site.get_questions_on_collectives(['co1', 'co2'])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_bountied_questions` ----


@lest.register
def test_get_bountied_questions_url() -> None:
    site.get_bountied_questions()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/questions/featured?site=stackoverflow')


@lest.register
def test_get_bountied_questions_return_value() -> None:
    res = site.get_bountied_questions()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_questions_with_no_answers` ----


@lest.register
def test_get_questions_with_no_answers_url() -> None:
    site.get_questions_with_no_answers()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'questions/no-answers?site=stackoverflow')


@lest.register
def test_get_questions_with_no_answers_return_value() -> None:
    res = site.get_questions_with_no_answers()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_unanswered_questions` ----


@lest.register
def test_get_unanswered_questions_url() -> None:
    site.get_unanswered_questions()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'questions/unanswered?site=stackoverflow')


@lest.register
def test_get_unanswered_questions_return_value() -> None:
    res = site.get_unanswered_questions()

    lest.assert_eq(res, [Item({'id': 1})])
