class BadArgumentsError(Exception):
    """Raises, when given arguments are invalid."""


class HttpError(Exception):
    """Raises, when API returns not 200 status code."""
    def __init__(self, code: int, api_ans: dict) -> None:
        """
        :param code: status code of the API response
        :param api_ans: JSON of the API response
        """
        super().__init__(code, api_ans)

        self.msg = f'{api_ans["error_message"]} (status code {code}).'

    def __str__(self) -> str:
        return self.msg


class AccessTokenOrAppKeyRequired(Exception):
    """Raises, when method requires access token or app key, but it's not set."""


class ChatLoginError(Exception):
    """Raises, when class `pystackapi.chat.Chat` can't login."""
