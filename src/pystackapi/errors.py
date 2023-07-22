class BadArgumentsError(Exception):
    """Raises, when given arguments are invalid."""


class HttpError(Exception):
    """Raises, when API returns not 200 status code."""
    def __init__(self, code: int, url: str) -> None:
        super().__init__(code, url)

        self.msg = ''
        match code:
            case 400:
                self.msg = f'Bad request for url {url}'
            case 401:
                self.msg = 'Acess token required'
            case 402:
                self.msg = 'Invalid acess token'
            case 403:
                self.msg = 'Acess denied'
            case 404:
                self.msg = f'Url {url} not found'
            case 405:
                self.msg = 'Key required'
            case 406:
                self.msg = 'Access token compromised'
            case 407:
                self.msg = 'Write failed'
            case 409:
                self.msg = 'Duplicate request'
            case 500:
                self.msg = 'Internal error'
            case 502:
                self.msg = 'Throttle violation'
            case 503:
                self.msg = 'Temporarily unavailable'

        if self.msg:
            self.msg += f' (status code {code}).'
        else:
            self.msg = str(code)

    def __str__(self) -> str:
        return self.msg
