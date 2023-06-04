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

    def call(self, query: str) -> Response:
        """Returns result of calling of `query` to API."""
        params = f'?site={self.name}'
        if self.api_key is not None:
            params += f'&access_token={self.api_key}'

        response = requests.get(f'{self.base_url}{query}{params}')

        if response.status_code != 200:
            raise HttpError(response.status_code)
        return Response(response.json())

    def get_info(self) -> Response:
        """Returns result of calling `/info` API method."""
        return self.call('info/')
