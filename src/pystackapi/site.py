from typing import Any, cast, TypedDict

import requests

from .errors import HttpError
from .item import Item


class ResponseDict(TypedDict):
    items: list[Item]
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

    def get(self, query: str, **kwargs: Any) -> ResponseDict:
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

        result = response.json()
        result['items'] = [Item(data) for data in result['items']]
        return cast(ResponseDict, result)  # we guarantee that `result` is `ResponseDict`.

    def get_info(self) -> ResponseDict:
        """Returns result of calling `/info` API method."""
        return self.get('info/')

    def get_users(self, ids: list[int] | None = None, **kwargs: Any) -> ResponseDict:
        """Returns result of calling `/users` API method."""
        if ids is not None:
            addition = ';'.join(map(str, ids))
        else:
            addition = ''
        return self.get(f'users/{addition}', **kwargs)

    def get_user(self, uid: int, **kwargs: Any) -> ResponseDict:
        return self.get_users([uid], **kwargs)

    def get_questions(self, ids: list[int] | None = None, **kwargs: Any) -> ResponseDict:
        """Returns result of calling `/questions` API method."""
        if ids is not None:
            addition = ';'.join(map(str, ids))
        else:
            addition = ''
        return self.get(f'questions/{addition}', **kwargs)

    def get_question(self, q_id: int, **kwargs: Any) -> ResponseDict:
        return self.get_questions([q_id], **kwargs)

    def get_answers(self, ids: list[int] | None = None, **kwargs: Any) -> ResponseDict:
        """Returns result of calling `/answers` API method."""
        if ids is not None:
            addition = ';'.join(map(str, ids))
        else:
            addition = ''
        return self.get(f'answers/{addition}', **kwargs)

    def get_answer(self, a_id: int, **kwargs: Any) -> ResponseDict:
        return self.get_questions([a_id], **kwargs)

    def get_badges_recipients(self, ids: list[int] | None = None, **kwargs: Any) -> ResponseDict:
        if ids is not None:
            url = 'badges/' + ';'.join(map(str, ids)) + '/recipients'
        else:
            url = 'badges/recipients'
        return self.get(url, **kwargs)

    def get_tag_based_badges(self, **kwargs: Any) -> ResponseDict:
        return self.get('badges/tags', **kwargs)
