from typing import cast

from bs4 import BeautifulSoup, Tag
import requests

from .errors import ChatLoginError


class Chat:
    """Implements the StackExchange chats client."""
    def __init__(self, email: str, password: str, host: str = 'stackexchange.com') -> None:
        self.host = host
        self._login(email, password)

    def _login(self, email: str, password: str) -> None:
        response = requests.get(f'https://{self.host}/users/login?returnurl=%%2f', {
                'email': email,
                'password': password
            })
        soup = BeautifulSoup(response.text, "html.parser")
        key_input = cast(Tag, soup.find('input', {'name': 'fkey'}))  # cast is only for MyPy
        if key_input is None:
            raise ChatLoginError("key input not found")
        self._key = key_input['value']
        print(self._key)
