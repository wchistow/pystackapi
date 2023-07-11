"""Tests for `Site.get_answers` and `Site.get_answer`."""
import lest

from pystackapi import site as site_m
from pystackapi.item import Item

from . import requests

site_m.__dict__['requests'] = requests
site = site_m.Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


@lest.register
def test_get_answers_without_ids() -> None:
    site.get_answers()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/answers/?site=stackoverflow')


@lest.register
def test_get_answers_with_ids() -> None:
    site.get_answers([1, 2])

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/answers/1;2?site=stackoverflow')


@lest.register
def test_return_value_of_get_answers() -> None:
    res = site.get_answers()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_answer() -> None:
    site.get_answer(1)

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/answers/1?site=stackoverflow')


@lest.register
def test_return_value_of_get_answer() -> None:
    res = site.get_answer(1)

    lest.assert_eq(res, Item({'id': 1}))
