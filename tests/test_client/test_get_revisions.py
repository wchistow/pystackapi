"""Tests for `Site.get_answers` and `Site.get_answer`."""
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
def test_get_revisions_url() -> None:
    site.get_revisions([1])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/revisions/1'
                                 f'?site=stackoverflow')


@lest.register
def test_get_revisions_return_value() -> None:
    res = site.get_revisions([1])

    lest.assert_eq(res, [Item({'id': 1})])
