"""Tests for `Site.get_badges`, `Site.get_badges_recipients` and `Site.get_tag_based_badges`."""
import lest

from pystackapi import site as site_m
from pystackapi.item import Item

from . import API_VERSION, requests

site_m.__dict__['requests'] = requests
site = site_m.Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


# ---- tests for `Site.get_badges` ----


@lest.register
def test_get_badges_url() -> None:
    site.get_badges()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/badges/'
                                 f'?site=stackoverflow')


@lest.register
def test_get_badges_return_value() -> None:
    res = site.get_badges()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_badges_recipients` ----


@lest.register
def test_get_badges_recipients_without_ids_url() -> None:
    site.get_badges_recipients()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/badges/recipients'
                                 f'?site=stackoverflow')


@lest.register
def test_get_badges_recipients_with_ids_url() -> None:
    site.get_badges_recipients([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/badges/1;2/'
                                 f'recipients?site=stackoverflow')


@lest.register
def test_get_badges_recipients_return_value() -> None:
    res = site.get_badges_recipients()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_tag_based_badges` ----


@lest.register
def test_get_tag_based_badges_url() -> None:
    site.get_tag_based_badges()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/badges/tags'
                                 f'?site=stackoverflow')


@lest.register
def test_get_tag_based_badges_return_value() -> None:
    res = site.get_tag_based_badges()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_non_tag_based_badges` ----


@lest.register
def test_get_non_tag_based_badges_url() -> None:
    site.get_non_tag_based_badges()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/badges/name'
                                 f'?site=stackoverflow')


@lest.register
def test_get_non_tag_based_badges_return_value() -> None:
    res = site.get_non_tag_based_badges()

    lest.assert_eq(res, [Item({'id': 1})])
