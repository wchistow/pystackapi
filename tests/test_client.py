"""Tests for class `pystackapi.Site`."""
import lest

from pystackapi import site as site_m
from pystackapi.errors import HttpError
from pystackapi.item import Item

from mocks import RequestsMock

requests = RequestsMock(return_items=[{'id': 1}])

site_m.__dict__['requests'] = requests
site = site_m.Site('stackoverflow')


@lest.setup
def reset_requests() -> None:
    requests.reset()


# ------------ Tests for `Site.get` ------------


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
def test_get_with_access_token() -> None:
    l_site = site_m.Site('stackoverflow', access_token='someaccesstoken')
    l_site.get('ghgh/')

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/ghgh/?site=stackoverflow&access_token=someaccesstoken')


@lest.register
def test_get_with_app_key() -> None:
    l_site = site_m.Site('stackoverflow', app_key='someappkey')
    l_site.get('ghgh/')

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/ghgh/?site=stackoverflow&key=someappkey')


@lest.register
def test_handling_error() -> None:
    l_requests = RequestsMock(status_code=400)

    site_m.__dict__['requests'] = l_requests
    l_site = site_m.Site('stackoverflow')

    with lest.assert_raises(HttpError):
        l_site.get('ghgh/')

    site_m.__dict__['requests'] = requests  # reset


@lest.register
def test_return_value_of_get() -> None:
    res = site.get('ghgh/')

    expected_result = {
        'items': [
            Item({'id': 1})
        ]
    }

    lest.assert_eq(res, expected_result)


# ------------ Tests for `Site.get_info` ------------


@lest.register
def test_get_info() -> None:
    site.get_info()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/info/?site=stackoverflow')


@lest.register
def test_return_value_of_get_info() -> None:
    res = site.get_info()

    lest.assert_eq(res, Item({'id': 1}))


# ------------ Tests for `Site.get_users` and `Site.get_user` ------------


@lest.register
def test_get_users_without_ids() -> None:
    site.get_users()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/users/?site=stackoverflow')


@lest.register
def test_get_users_with_ids() -> None:
    site.get_users([1, 2])

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/users/1;2?site=stackoverflow')


@lest.register
def test_return_value_of_get_users() -> None:
    res = site.get_users()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_user() -> None:
    site.get_user(1)

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/users/1?site=stackoverflow')


@lest.register
def test_return_value_of_get_user() -> None:
    res = site.get_user(1)

    lest.assert_eq(res, Item({'id': 1}))


# ------------ Tests for `Site.get_questions` and `Site.get_question` ------------


@lest.register
def test_get_questions_without_ids() -> None:
    site.get_questions()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/questions/?site=stackoverflow')


@lest.register
def test_get_questions_with_ids() -> None:
    site.get_questions([1, 2])

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/questions/1;2?site=stackoverflow')


@lest.register
def test_return_value_of_get_questions() -> None:
    res = site.get_questions()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_question() -> None:
    site.get_question(1)

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/questions/1?site=stackoverflow')


@lest.register
def test_return_value_of_get_question() -> None:
    res = site.get_question(1)

    lest.assert_eq(res, Item({'id': 1}))


# ------------ Tests for `Site.get_articles` and `Site.get_article` ------------


@lest.register
def test_get_articles_without_ids() -> None:
    site.get_articles()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/articles/?site=stackoverflow')


@lest.register
def test_get_articles_with_ids() -> None:
    site.get_articles([1, 2])

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/articles/1;2?site=stackoverflow')


@lest.register
def test_return_value_of_get_articles() -> None:
    res = site.get_articles()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_article() -> None:
    site.get_article(1)

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/articles/1?site=stackoverflow')


@lest.register
def test_return_value_of_get_article() -> None:
    res = site.get_article(1)

    lest.assert_eq(res, Item({'id': 1}))


# ------------ Tests for `Site.get_answers` and `Site.get_answer` ------------


@lest.register
def test_get_answers_without_ids() -> None:
    site.get_answers()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/answers/?site=stackoverflow')


@lest.register
def test_get_answers_with_ids() -> None:
    site.get_answers([1, 2])

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/answers/1;2?site=stackoverflow')


@lest.register
def test_return_value_of_get_answers() -> None:
    res = site.get_answers()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_answer() -> None:
    site.get_answer(1)

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/answers/1?site=stackoverflow')


@lest.register
def test_return_value_of_get_answer() -> None:
    res = site.get_answer(1)

    lest.assert_eq(res, Item({'id': 1}))


# ------------ Tests for `Site.get_badges_recipients` ------------


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


# ------------ Tests for `Site.get_tag_based_badges` ------------


@lest.register
def test_get_tag_based_badges() -> None:
    site.get_tag_based_badges()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/badges/tags?site=stackoverflow')


@lest.register
def test_return_value_of_get_tag_based_badges() -> None:
    res = site.get_tag_based_badges()

    lest.assert_eq(res, [Item({'id': 1})])


# ------------ Tests for `Site.get_collectives` and `get_collective` ------------


@lest.register
def test_get_collectives_without_slugs() -> None:
    site.get_collectives()

    lest.assert_eq(requests.url, 'https://api.stackexchange.com/2.3/collectives/?site=stackoverflow')


@lest.register
def test_get_collectives_with_slugs() -> None:
    site.get_collectives(['co1', 'co2'])

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/collectives/co1;co2?site=stackoverflow')


@lest.register
def test_return_value_of_get_collectives() -> None:
    res = site.get_collectives()

    lest.assert_eq(res, [Item({'id': 1})])


@lest.register
def test_get_collective() -> None:
    site.get_collective('co1')

    lest.assert_eq(requests.url,
                   'https://api.stackexchange.com/2.3/collectives/co1?site=stackoverflow')


@lest.register
def test_return_value_of_get_collective() -> None:
    res = site.get_collective('co1')

    lest.assert_eq(res, Item({'id': 1}))
