"""Tests for `Site.get_answers`, `Site.get_answer` and `Site.get_answers_on_collectives`."""
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
def test_get_answers_without_ids_url() -> None:
    site.get_answers()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/answers/'
                                 f'?site=stackoverflow')


@lest.register
def test_get_answers_with_ids_url() -> None:
    site.get_answers([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/answers/1;2'
                                 f'?site=stackoverflow')


@lest.register
def test_get_answers_return_value() -> None:
    res = site.get_answers()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_answer_url() -> None:
    site.get_answer(1)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/answers/1'
                                 f'?site=stackoverflow')


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
