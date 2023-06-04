import requests

from .errors import HttpError
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

    def get_users(self, ids: list | None = None):
        """Returns result of calling `/users` API method."""
        if ids is not None:
            ids_str = ';'.join(map(str, ids))
            return self.call(f'users/{ids_str}', **kwargs)
        else:
            return self.call('users/', **kwargs)
