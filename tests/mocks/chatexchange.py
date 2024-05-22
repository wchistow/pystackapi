"""Mock that replace the `chatexchange.Client` class."""


class ChatexchangeClientMock:
    def __init__(self, email: str | None = None, password: str | None = None) -> None:
        self.email = email
        self.password = password

    def reset(self) -> None:
        self.email = None
        self.password = None
