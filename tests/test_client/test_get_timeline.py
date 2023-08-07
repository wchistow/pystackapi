"""Tests for `Site.get_timeline_of_questions`."""
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
def test_get_timeline_of_questions_url() -> None:
    site.get_timeline_of_questions([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'questions/1;2/timeline?site=stackoverflow')


@lest.register
def test_get_timeline_of_questions_return_value() -> None:
    res = site.get_timeline_of_questions([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])
