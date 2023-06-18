from typing import Any

import requests

from .errors import HttpError
from .models import Question, User, Badge
from .response import Response


class Site:
    """Implements API client."""
    version = '2.3'
    base_url = f'https://api.stackexchange.com/{version}/'

    def __init__(self, name: str, api_key: str | None = None) -> None:
        self.name = name
        self.api_key = api_key

    def call(self, query: str, **kwargs: dict[str, Any]) -> Response:
        """Returns result of calling of `query` to API."""
        params = f'?site={self.name}'
        if self.api_key is not None:
            params += f'&access_token={self.api_key}'

        if kwargs:
            params += '&' + '&'.join((f'{k}={v}' for k, v in kwargs.items()))

        url = f'{self.base_url}{query}{params}'
        response = requests.get(url)

        if response.status_code != 200:
            raise HttpError(response.status_code, url)
        return Response(response.json())

    def get_info(self) -> Response:
        """Returns result of calling `/info` API method."""
        return self.call('info/')

    def get_users(self, ids: list[int] | None = None, **kwargs: Any) -> list[User]:
        """Returns result of calling `/users` API method."""
        if ids is not None:
            addition = ';'.join(map(str, ids))
        else:
            addition = ''
        response = self.call(f'users/{addition}', **kwargs)
        return [User(self, dict(data)) for data in response]

    def get_user(self, uid: int, **kwargs: Any) -> User:
        return self.get_users([uid], **kwargs)[0]

    def get_questions(self, ids: list[int] | None = None, **kwargs: Any) -> list[Question]:
        """Returns result of calling `/questions` API method."""
        if ids is not None:
            addition = ';'.join(map(str, ids))
        else:
            addition = ''
        response = self.call(f'questions/{addition}', **kwargs)
        return [Question(self, dict(data)) for data in response]

    def get_question(self, q_id: int, **kwargs: Any) -> Question:
        return self.get_questions([q_id], **kwargs)[0]

    def get_badges_recipients(self, ids: list[int] | None = None, **kwargs: Any) -> list[Badge]:
        if ids is not None:
            url = 'badges/' + ';'.join(map(str, ids)) + '/recipients'
        else:
            url = 'badges/recipients'
        response = self.call(url, **kwargs)
        return [Badge(self, dict(data)) for data in response]

    def get_tag_based_badges(self, **kwargs: Any) -> list[Badge]:
        return [Badge(self, dict(data)) for data in self.call('badges/tags', **kwargs)]
