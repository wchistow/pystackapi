"""
Tests for
`Site.get_tags`, `Site.get_tags_on_collectives`,
`Site.get_tags_info`, `Site.get_tags_faq`,
`Site.get_moderator_only_tags`, `Site.get_required_tags`,
`Site.get_tags_synonyms`, `Site.get_related_tags`,
`Site.get_top_answerers_on_tag`, `Site.get_top_askers_on_tag`,
`Site.get_tags_wikis`, `Site.get_users_tags`,
`Site.get_user_top_answers_on_tags`, `Site.get_user_top_answers_tags`,
`Site.get_user_top_questions_tags` and `Site.get_user_top_tags`.
"""
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


# ---- tests for `Site.get_tags` ----


@lest.register
def test_get_tags_url() -> None:
    site.get_tags()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/tags?site=stackoverflow')


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


# ---- tests for `Site.get_required_tags` ----


@lest.register
def test_get_required_tags_url() -> None:
    site.get_required_tags()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/tags/required?site=stackoverflow')


@lest.register
def test_get_required_tags_return_value() -> None:
    res = site.get_required_tags()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_required_tags` ----


@lest.register
def test_get_tags_synonyms_without_tags_url() -> None:
    site.get_tags_synonyms()

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/tags/synonyms?site=stackoverflow')


@lest.register
def test_get_tags_synonyms_with_tags_url() -> None:
    site.get_tags_synonyms(['python', 'pandas'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/tags/python;pandas/synonyms?site=stackoverflow')


@lest.register
def test_get_required_tags_return_value() -> None:
    res = site.get_required_tags()

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_required_tags` ----


@lest.register
def test_get_related_tags_url() -> None:
    site.get_related_tags(['python', 'pandas'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/tags/python;pandas/related?site=stackoverflow')


@lest.register
def test_get_related_tags_return_value() -> None:
    res = site.get_related_tags(['python', 'pandas'])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_top_answerers_on_tag` ----


@lest.register
def test_get_top_answerers_on_tag_url() -> None:
    site.get_top_answerers_on_tag('python', period='month')

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/tags/python/top-answerers/month?site=stackoverflow')


@lest.register
def test_get_top_answerers_on_tag_return_value() -> None:
    res = site.get_top_answerers_on_tag('python', period='month')

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_top_askers_on_tag` ----


@lest.register
def test_get_top_askers_on_tag_url() -> None:
    site.get_top_askers_on_tag('python', period='month')

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/tags/python/top-askers/month?site=stackoverflow')


@lest.register
def test_get_top_askers_on_tag_return_value() -> None:
    res = site.get_top_askers_on_tag('python', period='month')

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_tags_wikis` ----


@lest.register
def test_get_tags_wikis_url() -> None:
    site.get_tags_wikis(['python', 'pandas'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/tags/python;pandas/wikis?site=stackoverflow')


@lest.register
def test_get_tags_wikis_return_value() -> None:
    res = site.get_tags_wikis(['python', 'pandas'])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_users_tags` ----


@lest.register
def test_get_users_tags_url() -> None:
    site.get_users_tags([1, 2])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/users/1;2/tags?site=stackoverflow')


@lest.register
def test_get_users_tags_return_value() -> None:
    res = site.get_users_tags([1, 2])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_user_top_answers_on_tags` ----


@lest.register
def test_get_user_top_answers_on_tags_url() -> None:
    site.get_user_top_answers_on_tags(1, ['python', 'pandas'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/users/1/tags/python;pandas/top-answers?site=stackoverflow')


@lest.register
def test_get_user_top_answers_on_tags_return_value() -> None:
    res = site.get_user_top_answers_on_tags(1, ['python', 'pandas'])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_user_top_questions_on_tags` ----


@lest.register
def test_get_user_top_questions_on_tags_url() -> None:
    site.get_user_top_questions_on_tags(1, ['python', 'pandas'])

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/users/1/tags/python;pandas/top-questions?site=stackoverflow')


@lest.register
def test_get_user_top_questions_on_tags_return_value() -> None:
    res = site.get_user_top_questions_on_tags(1, ['python', 'pandas'])

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_user_top_answers_tags` ----


@lest.register
def test_get_user_top_answers_tags_url() -> None:
    site.get_user_top_answers_tags(1)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/users/1/top-answer-tags?site=stackoverflow')


@lest.register
def test_get_user_top_answers_tags_return_value() -> None:
    res = site.get_user_top_answers_tags(1)

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_user_top_questions_tags` ----


@lest.register
def test_get_user_top_questions_tags_url() -> None:
    site.get_user_top_questions_tags(1)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/users/1/top-question-tags?site=stackoverflow')


@lest.register
def test_get_user_top_questions_tags_return_value() -> None:
    res = site.get_user_top_questions_tags(1)

    lest.assert_eq(res, [Item({'id': 1})])


# ---- tests for `Site.get_user_top_tags` ----


@lest.register
def test_get_user_top_tags_url() -> None:
    site.get_user_top_tags(1)

    lest.assert_eq(requests.url, f'https://api.stackexchange.com/{API_VERSION}'
                                 '/users/1/top-tags?site=stackoverflow')


@lest.register
def test_get_user_top_tags_return_value() -> None:
    res = site.get_user_top_tags(1)

    lest.assert_eq(res, [Item({'id': 1})])
