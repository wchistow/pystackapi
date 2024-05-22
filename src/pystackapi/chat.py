from chatexchange import Client  # type: ignore[import-untyped]


class Chat:
    """Wrapper for class `chatexchange.Client`."""
    def __init__(self, email: str | None = None, password: str | None = None) -> None:
        self._client = Client(email=email, password=password)
