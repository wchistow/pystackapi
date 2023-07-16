from typing import Any, cast, TypedDict

import requests

from .errors import BadArgumentsError, HttpError
from .item import Item


class RawResponseDict(TypedDict):
    items: list[dict]
    has_more: bool
    quota_max: int
    quota_remaining: int


class Site:
    """Implements API client."""
    version = '2.3'
    base_url = f'https://api.stackexchange.com/{version}/'

    def __init__(self, name: str, access_token: str | None = None,
                 app_key: str | None = None) -> None:
        self.name = name
        self.access_token = access_token
        self.app_key = app_key

    def get(self, query: str, **kwargs: Any) -> RawResponseDict:
        """Returns raw result of calling `query` to API."""
        params = f'?site={self.name}'
        if self.access_token is not None:
            params += f'&access_token={self.access_token}'
        if self.app_key is not None:
            params += f'&key={self.app_key}'

        if kwargs:
            params += '&' + '&'.join((f'{k}={v}' for k, v in kwargs.items()))

        url = f'{self.base_url}{query}{params}'
        response = requests.get(url)

        if response.status_code != 200:
            raise HttpError(response.status_code, url)

        # we guarantee that `response.json` is `RawResponseDict`.
        return cast(RawResponseDict, response.json())

    # CONTRIBUTORS: Please, sort methods by alphabet in pairs
    # with first `get_<plural>` and then, get_<singular>`.

    def get_answers(self, ids: list[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, all the undeleted answers in the system,
        else the set of answers identified by `ids`.
        """
        addition = ';'.join(map(str, ids or []))
        return [Item(data) for data in self.get(f'answers/{addition}', **kwargs)['items']]

    def get_answer(self, a_id: int, **kwargs: Any) -> Item | None:
        """
        Returns answer identified by `a_id`.
        Returns `None` if requested object don't found.
        """
        try:
            return self.get_answers([a_id], **kwargs)[0]
        except IndexError:
            return None

    def get_articles(self, ids: list[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, all articles on the site,
        else the articles identified by `ids`.
        """
        addition = ';'.join(map(str, ids or []))
        return [Item(data) for data in self.get(f'articles/{addition}', **kwargs)['items']]

    def get_article(self, a_id: int, **kwargs: Any) -> Item | None:
        """
        Returns article identified by `a_id`.
        Returns `None` if requested object don't found.
        """
        try:
            return self.get_articles([a_id], **kwargs)[0]
        except IndexError:
            return None

    def get_badges(self, **kwargs: Any) -> list[Item]:
        """Returns all badges in the system."""
        return [Item(data) for data in self.get('badges/', **kwargs)['items']]

    def get_badges_recipients(self, ids: list[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, recently awarded badges in the system,
        constrained to a certain set of badges, else recently awarded badges in the system.
        """
        if ids is not None:
            url = 'badges/' + ';'.join(map(str, ids)) + '/recipients'
        else:
            url = 'badges/recipients'
        return [Item(data) for data in self.get(url, **kwargs)['items']]

    def get_tag_based_badges(self, **kwargs: Any) -> list[Item]:
        """Returns the badges that are awarded for participation in specific tags."""
        return [Item(data) for data in self.get('badges/tags', **kwargs)['items']]

    def get_collectives(self, slugs: list[str] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `slugs` is set, collectives in `slugs` found on the site,
        else, all collectives in the system.
        """
        addition = ';'.join(map(str, slugs or []))
        return [Item(data) for data in self.get(f'collectives/{addition}', **kwargs)['items']]

    def get_collective(self, slug: str, **kwargs: Any) -> Item | None:
        """
        Returns collective with specific `slug`.
        Returns `None` if requested object don't found.
        """
        try:
            return self.get_collectives([slug], **kwargs)[0]
        except IndexError:
            return None

    def get_comments(self, ids: list[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, the comments identified in `ids`,
        else, all comments on the site.
        """
        addition = ';'.join(map(str, ids or []))
        return [Item(data) for data in self.get(f'comments/{addition}', **kwargs)['items']]

    def get_comment(self, c_id: int, **kwargs: Any) -> Item | None:
        """
        Returns the comment identified in `c_id`.
        Returns `None` if requested object don't found.
        """
        try:
            return self.get_comments([c_id], **kwargs)[0]
        except IndexError:
            return None

    def get_info(self) -> Item:
        """Returns a collection of statistics about the site."""
        return Item(self.get('info/')['items'][0])  # here can't be `IndexError`

    def get_privileges(self, **kwargs: Any) -> list[Item]:
        """Returns the earnable privileges on a site."""
        return [Item(data) for data in self.get('privileges/', **kwargs)['items']]

    def get_questions(self, ids: list[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, all the undeleted questions in the system,
        else the set of questions identified by `ids`.
        """
        addition = ';'.join(map(str, ids or []))
        return [Item(data) for data in self.get(f'questions/{addition}', **kwargs)['items']]

    def get_question(self, q_id: int, **kwargs: Any) -> Item | None:
        """
        Returns the question identified in `q_id`.
        Returns `None` if requested object don't found.
        """
        try:
            return self.get_questions([q_id], **kwargs)[0]
        except IndexError:
            return None

    def get_revisions(self, ids: list[int], **kwargs: Any) -> list[Item]:
        """Returns edit revisions identified by `ids`."""
        addition = ';'.join(map(str, ids or []))
        return [Item(data) for data in self.get(f'revisions/{addition}', **kwargs)['items']]

    def search(self, **kwargs: Any) -> list[Item]:
        """
        Searches a site for any questions which fit the given criteria.
        **Warning:** one of `tagged` or `intitle` keyword arguments must be set.
        """
        if 'tagged' not in kwargs and 'intitle' not in kwargs:
            raise BadArgumentsError('one of `tagged` or `intitle` keyword arguments must be set.')

        return [Item(data) for data in self.get('search/', **kwargs)['items']]

    def advanced_search(self, **kwargs: Any) -> list[Item]:
        """Searches a site for any questions which fit the given criteria."""
        return [Item(data) for data in self.get('search/advanced/', **kwargs)['items']]

    def get_similar(self, title: str, **kwargs: Any) -> list[Item]:
        """
        Returns questions which are similar to a hypothetical one based
        on a title and tag combination.
        """
        return [Item(data) for data in self.get('similar/', title=title, **kwargs)['items']]

    def get_tags(self, **kwargs: Any) -> list[Item]:
        """Returns all tags in the system."""
        return [Item(data) for data in self.get('tags/', **kwargs)['items']]

    def get_users(self, ids: list[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, the users identified by `ids`,
        else all users on a site.
        """
        addition = ';'.join(map(str, ids or []))
        return [Item(data) for data in self.get(f'users/{addition}', **kwargs)['items']]

    def get_user(self, uid: int, **kwargs: Any) -> Item | None:
        """
        Returns the user identified in `uid`.
        Returns `None` if requested object don't found.
        """
        try:
            return self.get_users([uid], **kwargs)[0]
        except IndexError:
            return None
