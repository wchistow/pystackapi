"""Mock that replace the `requests` library."""


class RequestsMock:
    def __init__(self,
                 return_items: list | None = None,
                 status_code: int = 200,
                 no_data: list[str] | None = None) -> None:
        """
        :param return_items: what is in the `'items'` key of response
        :param status_code: what is status code of response
        :param no_data: on which urls key `'items'` should be empty
        """
        self.return_items = return_items or []
        self.status_code = status_code
        self.no_data = no_data or []

        self.url: str | None = None
        self.data: dict | None = None  # only for POST-requests

    def get(self, url: str) -> 'ResponseMock':
        self.url = url
        if url in self.no_data:
            items = []
        else:
            items = self.return_items

        if self.status_code == 200:
            return ResponseMock(self.status_code, {'items': items})
        else:
            return ResponseMock(self.status_code, {'error_message': 'some error'})

    def post(self, url: str, data: dict) -> 'ResponseMock':
        self.url = url
        self.data = data

        if url in self.no_data:
            items = []
        else:
            items = self.return_items

        if self.status_code == 200:
            return ResponseMock(self.status_code, {'items': items})
        else:
            return ResponseMock(self.status_code, {'error_message': 'some error'})

    def reset(self) -> None:
        self.url = None
        self.data = None


class ResponseMock:
    """Implements HTTP response."""
    def __init__(self, status_code: int, data: dict) -> None:
        self.status_code = status_code
        self.data = data

    def json(self) -> dict:
        return self.data
