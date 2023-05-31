import requests


class Client:
    version = '2.3'
    base_url = f'api.stackexchange.org/{version}'

    def __init__(self, site: str, api_key: str | None = None):
        self.site = site
        self.api_key = api_key
