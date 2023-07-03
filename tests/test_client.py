"""Tests for class `pystackapi.Site`."""
import lest

from pystackapi import site as site_m

from mocks import RequestsMock

requests = RequestsMock()

site_m.__dict__['requests'] = requests
site = site_m.Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


@lest.register
def test_simple_get() -> None:
    site.get('ghgh/')

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/ghgh/?site=stackoverflow')


@lest.register
def test_get_with_kwargs() -> None:
    site.get('ghgh/', arg1='hello')

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/ghgh/?site=stackoverflow&arg1=hello')


@lest.register
def test_get_info() -> None:
    site.get_info()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/info/?site=stackoverflow')


@lest.register
def test_get_users_without_ids() -> None:
    site.get_users()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/users/?site=stackoverflow')


@lest.register
def test_get_users_with_one_id() -> None:
    site.get_users([1])

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/users/1?site=stackoverflow')


@lest.register
def test_get_users_with_many_ids() -> None:
    site.get_users([1, 2])

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/users/1;2?site=stackoverflow')


@lest.register
def test_get_questions_without_ids() -> None:
    site.get_questions()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/questions/?site=stackoverflow')


@lest.register
def test_get_questions_with_one_id() -> None:
    site.get_questions([1])

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/questions/1?site=stackoverflow')


@lest.register
def test_get_questions_with_many_ids() -> None:
    site.get_questions([1, 2])

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/questions/1;2?site=stackoverflow')


@lest.register
def test_get_badges_recipients_without_ids() -> None:
    site.get_badges_recipients()

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/badges/recipients?site=stackoverflow')


@lest.register
def test_get_badges_recipients_with_one_id() -> None:
    site.get_badges_recipients([1])

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/badges/1/recipients?site=stackoverflow')


@lest.register
def test_get_badges_recipients_with_many_ids() -> None:
    site.get_badges_recipients([1, 2])

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/badges/1;2/recipients?site=stackoverflow')


@lest.register
def test_get_tag_based_badges() -> None:
    site.get_tag_based_badges()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/badges/tags?site=stackoverflow')
