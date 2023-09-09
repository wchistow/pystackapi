from typing import Any, Iterable

from ._base_client import BaseClient
from ._raw_response_dict import RawResponseDict
from ._utils import _join_with_semicolon
from .item import Item


class Network(BaseClient):
    """Implements the StackExchange APIs client for all SE network."""
    version = '2.3'
    base_url = f'https://api.stackexchange.com/{version}/'

    def get(self, query: str, **kwargs: Any) -> RawResponseDict:
        """Returns raw result of calling `query` to API."""
        return self._call(f'{self.base_url}{query}', kwargs)

    def get_access_tokens(self, access_tokens: Iterable[str], **kwargs: Any) -> list[Item]:
        """Returns the properties for a set of access tokens."""
        return [Item(data) for data in
                self.get(f'access-tokens/{_join_with_semicolon(access_tokens)}', **kwargs)['items']]

    def invalidate_access_tokens(self, access_tokens: Iterable[str], **kwargs: Any) -> list[Item]:
        """
        Immediately expires the access tokens passed.
        This method is meant to allow an application to discard any active access tokens
        it no longer needs. Returns list of access tokens.
        """
        return [Item(data) for data in
                self.get(f'access-tokens/{_join_with_semicolon(access_tokens)}/invalidate',
                         **kwargs)['items']]

    def get_errors(self, **kwargs: Any) -> list[Item]:
        """Returns the various error codes that can be produced by the API."""
        return [Item(data) for data in self.get('errors', **kwargs)['items']]

    def simulate_error(self, code: int, **kwargs: Any) -> Any:
        """This method allows you to generate an error."""
        self.get(f'errors/{code}', **kwargs)

    def create_filter(self, **kwargs: Any) -> Item:
        """
        Creates a new filter given a list of includes, excludes, a base filter,
        and whether this filter should be "unsafe".

        It is not expected that many applications will call this method at runtime,
        filters should be pre-calculated and "baked in" in the common cases.
        """
        return Item(self.get('filters/create', **kwargs)['items'][0])
