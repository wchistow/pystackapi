class BadArgumentsError(Exception):
    """Raises, when given arguments are invalid."""


class HttpError(Exception):
    """Raises, when API returns not 200 status code."""
    def __init__(self, code: int, url: str) -> None:
        super().__init__(code, url)

        self.msg = ''
        match code:
            case 400:
                self.msg = 'An malformed parameter was passed'
            case 401:
                self.msg = 'No access_token was passed'
            case 402:
                self.msg = ('An access_token that is malformed, expired,'
                            ' or otherwise incorrect was passed')
            case 403:
                self.msg = 'The access_token passed does not have sufficient permissions'
            case 404:
                self.msg = 'No matching method was found'
            case 405:
                self.msg = 'No key was passed'
            case 406:
                self.msg = 'Access token may have been leaked, it will be invalidated'
            case 407:
                self.msg = 'A write operation was rejected'
            case 409:
                self.msg = 'A request identified by the given request_id has already been run'
            case 500:
                self.msg = ('An error was encountered while servicing this request,'
                            ' it has been recorded')
            case 502:
                self.msg = ('Some violation of the throttling or request quota contract'
                            ' was encountered')
            case 503:
                self.msg = 'he method, or the entire API, is temporarily unavailable'

        if self.msg:
            self.msg = f'"{self.msg}" on URL {url} (status code {code}).'
        else:
            self.msg = str(code)

    def __str__(self) -> str:
        return self.msg


class AccessTokenOrAppKeyRequired(Exception):
    """Raises, when method requires access token, but it's not set."""
