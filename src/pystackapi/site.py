from typing import Any, cast, TypedDict

import requests

from .errors import HttpError
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
        """Returns result of calling of `query` to API."""
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

    def get_info(self) -> Item:
        """Returns result of calling `/info` API method."""
        return Item(self.get('info/')['items'][0])

    def get_users(self, ids: list[int] | None = None, **kwargs: Any) -> list[Item]:
        """Returns result of calling `/users` API method."""
        addition = ';'.join(map(str, ids or []))
        return [Item(data) for data in self.get(f'users/{addition}', **kwargs)['items']]

    def get_user(self, uid: int, **kwargs: Any) -> Item:
        return self.get_users([uid], **kwargs)[0]

    def get_questions(self, ids: list[int] | None = None, **kwargs: Any) -> list[Item]:
        """Returns result of calling `/questions` API method."""
        addition = ';'.join(map(str, ids or []))
        return [Item(data) for data in self.get(f'questions/{addition}', **kwargs)['items']]

    def get_question(self, q_id: int, **kwargs: Any) -> Item:
        return self.get_questions([q_id], **kwargs)[0]

    def get_answers(self, ids: list[int] | None = None, **kwargs: Any) -> list[Item]:
        """Returns result of calling `/answers` API method."""
        addition = ';'.join(map(str, ids or []))
        return [Item(data) for data in self.get(f'answers/{addition}', **kwargs)['items']]

    def get_answer(self, a_id: int, **kwargs: Any) -> Item:
        return self.get_answers([a_id], **kwargs)[0]

    def get_articles(self, ids: list[int] | None = None, **kwargs: Any) -> list[Item]:
        """Returns result of calling `/articles` API method."""
        addition = ';'.join(map(str, ids or []))
        return [Item(data) for data in self.get(f'articles/{addition}', **kwargs)['items']]

    def get_article(self, a_id: int, **kwargs: Any) -> Item:
        return self.get_articles([a_id], **kwargs)[0]

    def get_badges_recipients(self, ids: list[int] | None = None, **kwargs: Any) -> list[Item]:
        if ids is not None:
            url = 'badges/' + ';'.join(map(str, ids)) + '/recipients'
        else:
            url = 'badges/recipients'
        return [Item(data) for data in self.get(url, **kwargs)['items']]

    def get_tag_based_badges(self, **kwargs: Any) -> list[Item]:
        return [Item(data) for data in self.get('badges/tags', **kwargs)['items']]
