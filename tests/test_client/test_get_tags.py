"""
Tests for
`Site.get_tags`, `Site.get_tags_on_collectives`,
`Site.get_tags_info`, `Site.get_tags_faq` and
`Site.get_moderator_only_tags`.
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


# ---- tests for `Site.get_tags_info` ----


@lest.register
def test_get_tags_info_url() -> None:
    site.get_tags_info(['python', 'pandas'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/tags/python;pandas/info?site=stackoverflow')


@lest.register
def test_get_tags_info_return_value() -> None:
    res = site.get_tags_info(['python', 'pandas'])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_tags_faq` ----


@lest.register
def test_get_tags_faq_url() -> None:
    site.get_tags_faq(['python', 'pandas'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/tags/python;pandas/faq?site=stackoverflow')


@lest.register
def test_get_tags_faq_return_value() -> None:
    res = site.get_tags_faq(['python', 'pandas'])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_moderator_only_tags` ----


@lest.register
def test_get_moderator_only_tags_url() -> None:
    site.get_moderator_only_tags()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/tags/moderator-only?site=stackoverflow')


@lest.register
def test_get_moderator_only_tags_return_value() -> None:
    res = site.get_moderator_only_tags()

    lest.assert_eq(res, [Item({'id': 1})])
