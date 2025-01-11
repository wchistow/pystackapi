"""Mock that replace the `chatexchange.Client` class."""


class ChatexchangeClientMock:
    def __init__(self, email: str, password: str, host: str = 'stackexchange.com') -> None:
        self.email = email
        self.password = password
        self.host = host

    def reset(self) -> None:
        self.email = None
        self.password = None
