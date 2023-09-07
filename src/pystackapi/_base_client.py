from typing import cast

import requests

from .errors import HttpError
from ._raw_response_dict import RawResponseDict


class BaseClient:
    """Base class for clients of the StackExchange API."""
    def _call(self, url: str, params: dict) -> RawResponseDict:
        req_params = ('?' if params else '') + '&'.join(f'{k}={v}' for k, v in params.items())

        response = requests.get(f'{url}{req_params}')

        if response.status_code != 200:
            raise HttpError(response.status_code, url)

        # we guarantee that `response.json` is `RawResponseDict`.
        return cast(RawResponseDict, response.json())
