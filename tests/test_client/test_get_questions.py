"""Tests for `Site.get_questions` and `Site.get_question`."""
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
def test_get_questions_without_ids_url() -> None:
    site.get_questions()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/questions/?site=stackoverflow')


@lest.register
def test_get_questions_with_ids_url() -> None:
    site.get_questions([1, 2])

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/questions/1;2?site=stackoverflow')


@lest.register
def test_get_questions_return_value() -> None:
    res = site.get_questions()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_question_url() -> None:
    site.get_question(1)

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/questions/1?site=stackoverflow')


@lest.register
def test_get_question_return_value() -> None:
    res = site.get_question(1)

    lest.assert_eq(res, Item({'id': 1}))
