"""Tests for `Site.get_related_to_questions`."""
import lest

from pystackapi import _base_client as client_m
from pystackapi import Site
from pystackapi.item import Item

from main import API_VERSION, requests

client_m.__dict__['requests'] = requests
site = Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


@lest.register
def test_get_related_to_questions_url() -> None:
    site.get_related_to_questions([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/'
                                 'questions/1;2/related?site=stackoverflow')


@lest.register
def tes_get_related_to_questions_return_value() -> None:
    res = site.get_related_to_questions([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])
