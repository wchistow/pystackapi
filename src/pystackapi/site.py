from typing import Any

import requests

from .errors import HttpError
from .models import Question
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

        params += '&' + '&'.join((f'{k}={v}' for k, v in kwargs.items()))

        response = requests.get(f'{self.base_url}{query}{params}')

        if response.status_code != 200:
            raise HttpError(response.status_code)
        return Response(response.json())

    def get_info(self) -> Response:
        """Returns result of calling `/info` API method."""
        return self.call('info/')

    def get_users(self, ids: list[int] | None = None, **kwargs: Any) -> Response:
        """Returns result of calling `/users` API method."""
        if ids is not None:
            ids_str = ';'.join(map(str, ids))
            return self.call(f'users/{ids_str}', **kwargs)
        else:
            return self.call('users/', **kwargs)

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
