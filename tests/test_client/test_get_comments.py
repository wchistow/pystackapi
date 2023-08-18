"""
Tests for `Site.get_comments`, `Site.get_comment`,
`Site.get_comments_on_answers`, `Site.get_comments_on_articles`,
`Site.get_comments_on_questions`, `Site.get_comments_on_posts`,
`Site.get_users_comments` and `Site.get_users_comments_to`.
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


# ---- tests for `Site.get_comments` ----


@lest.register
def test_get_comments_without_ids_url() -> None:
    site.get_comments()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/comments/'
                                 '?site=stackoverflow')


@lest.register
def test_get_comments_with_ids_url() -> None:
    site.get_comments([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/comments/1;2'
                                 '?site=stackoverflow')


@lest.register
def test_get_comments_return_value() -> None:
    res = site.get_comments()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_comment` ----


@lest.register
def test_get_comment_url() -> None:
    site.get_comment(1)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/comments/1'
                                 '?site=stackoverflow')


@lest.register
def test_get_comment_return_value() -> None:
    res = site.get_comment(1)

    lest.assert_eq(res, Item({'id': 1}))


@lest.register
def test_get_comment_with_no_data() -> None:
    requests.no_data = [
        f'https://api.stackexchange.com/{API_VERSION}/comments/1?site=stackoverflow'
    ]

    res = site.get_comment(1)

    lest.assert_true(res is None)

    requests.no_data = []


# ---- tests for `Site.get_comments_on_answers` ---


@lest.register
def test_get_comments_on_answers_url() -> None:
    site.get_comments_on_answers([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/answers/1;2/'
                                 'comments?site=stackoverflow')


@lest.register
def test_get_comments_on_answers_return_value() -> None:
    res = site.get_comments_on_answers([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_comments_on_articles` ---


@lest.register
def test_get_comments_on_articles_url() -> None:
    site.get_comments_on_articles([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/articles/1;2/'
                                 'comments?site=stackoverflow')


@lest.register
def test_get_comments_on_articles_return_value() -> None:
    res = site.get_comments_on_articles([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_comments_on_questions` ----


@lest.register
def test_get_comments_on_questions_url() -> None:
    site.get_comments_on_questions([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/questions/1;2/'
                                 'comments?site=stackoverflow')


@lest.register
def test_get_comments_on_questions_return_value() -> None:
    res = site.get_comments_on_questions([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_comments_on_posts` ----


@lest.register
def test_get_comments_on_posts_url() -> None:
    site.get_comments_on_posts([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/posts/1;2/'
                                 'comments?site=stackoverflow')


@lest.register
def test_get_comments_on_posts_return_value() -> None:
    res = site.get_comments_on_posts([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_users_comments` ----


@lest.register
def test_get_users_comments_url() -> None:
    site.get_users_comments([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/users/1;2/'
                                 'comments?site=stackoverflow')


@lest.register
def test_get_users_comments_return_value() -> None:
    res = site.get_users_comments([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_users_comments_to` ----


@lest.register
def test_get_users_comments_to_url() -> None:
    site.get_users_comments_to([1, 2], 3)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}/users/1;2/'
                                 'comments/3?site=stackoverflow')


@lest.register
def test_get_users_comments_to_return_value() -> None:
    res = site.get_users_comments_to([1, 2], 3)

    lest.assert_eq(res, [Item({'id': 1})])
