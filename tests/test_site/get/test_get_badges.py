"""
Tests for `Site.get_badges`, `Site.get_badges_recipients`,
`Site.get_tag_based_badges` and `Site.get_users_badges`."""
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


# ---- tests for `Site.get_badges` ----


@lest.register
def test_get_badges_url() -> None:
    site.get_badges()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/badges?site=stackoverflow')


@lest.register
def test_get_badges_return_value() -> None:
    res = site.get_badges()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_badges_recipients` ----


@lest.register
def test_get_badges_recipients_without_ids_url() -> None:
    site.get_badges_recipients()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/badges/recipients'
                                 '?site=stackoverflow')


@lest.register
def test_get_badges_recipients_with_ids_url() -> None:
    site.get_badges_recipients([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/badges/1;2/'
                                 'recipients?site=stackoverflow')


@lest.register
def test_get_badges_recipients_return_value() -> None:
    res = site.get_badges_recipients()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_tag_based_badges` ----


@lest.register
def test_get_tag_based_badges_url() -> None:
    site.get_tag_based_badges()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/badges/tags'
                                 '?site=stackoverflow')


@lest.register
def test_get_tag_based_badges_return_value() -> None:
    res = site.get_tag_based_badges()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_non_tag_based_badges` ----


@lest.register
def test_get_non_tag_based_badges_url() -> None:
    site.get_non_tag_based_badges()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/badges/name'
                                 '?site=stackoverflow')


@lest.register
def test_get_non_tag_based_badges_return_value() -> None:
    res = site.get_non_tag_based_badges()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_users_badges` ----


@lest.register
def test_get_users_badges_url() -> None:
    site.get_users_badges([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/users/1;2/'
                                 'badges?site=stackoverflow')


@lest.register
def test_get_users_badges_return_value() -> None:
    res = site.get_users_badges([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])
