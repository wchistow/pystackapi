import requests

from .errors import HttpError
from .response import Response


class Client:
    version = '2.3'
    base_url = f'https://api.stackexchange.com/{version}/'

    def __init__(self, site: str, api_key: str | None = None) -> None:
        self.site = site
        self.api_key = api_key

    def call(self, query: str) -> Response:
        params = f'?site={self.site}'
        if self.api_key is not None:
            params += f'&access_token={self.api_key}'

        response = requests.get(f'{self.base_url}{query}{params}')

        if response.status_code != 200:
            raise HttpError(response.status_code)
        return Response(response.json())
