"""Tests for `Site.get_tags` and `Site.get_tags_on_collectives`."""
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
def test_get_tags_url() -> None:
    site.get_tags()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/tags/'
                                 '?site=stackoverflow')


@lest.register
def test_get_tags_return_value() -> None:
    res = site.get_tags()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_tags_on_collectives` ----


@lest.register
def test_get_tags_on_collectives_url() -> None:
    site.get_tags_on_collectives(['co1', 'co2'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/collectives/co1;co2/tags?site=stackoverflow')


@lest.register
def test_get_tags_on_collectives_return_value() -> None:
    res = site.get_tags_on_collectives(['co1', 'co2'])

    lest.assert_eq(res, [Item({'id': 1})])
