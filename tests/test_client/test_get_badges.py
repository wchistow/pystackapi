"""Tests for `Site.get_badges_recipients` and `Site.get_tag_based_badges`."""
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
def test_get_badges_recipients_without_ids() -> None:
    site.get_badges_recipients()

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/badges/recipients?site=stackoverflow')


@lest.register
def test_get_badges_recipients_with_ids() -> None:
    site.get_badges_recipients([1, 2])

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/badges/1;2/recipients?site=stackoverflow')


@lest.register
def test_return_value_of_get_badges_recipients() -> None:
    res = site.get_badges_recipients()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_tag_based_badges() -> None:
    site.get_tag_based_badges()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/badges/tags?site=stackoverflow')


@lest.register
def test_return_value_of_get_tag_based_badges() -> None:
    res = site.get_tag_based_badges()

    lest.assert_eq(res, [Item({'id': 1})])