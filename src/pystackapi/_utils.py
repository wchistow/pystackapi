"""Utils for clients."""
from typing import Any, Iterable, NoReturn

from .errors import AccessTokenOrAppKeyRequired, BadArgumentsError


def _join_with_semicolon(data: Iterable[Any]) -> str:
    return ';'.join(map(str, data))


def _check_iterable_is_not_empty(iterable: Iterable,  # type: ignore[return]
                                 arg_name: str = 'ids') -> None | NoReturn:
    """
    Raises `BadArgumentsError` with message
    "`the \\`{arg_name}\\` argument can't be an empty iterable object.`" if `iterable` is empty.

    :param arg_name: argument name for error message. Default - `"ids"`.
    """
    if not iterable:
        raise BadArgumentsError(
            f'the `{arg_name}` argument can\'t be an empty iterable object.'
        )


def _check_iterable_arg(iterable: Iterable | None, arg_name: str = 'ids') -> Iterable | NoReturn:
    """
    Raises `BadArgumentsError` with message
    "`the \\`{arg_name}\\` argument should be a non-empty iterable object.`"
    if `iterable` is empty, and it's not `None`.

    If `iterable` is `None`, returns empty list (`[]`).

    If `iterable` is not `None`, and it's not empty, returns `iterable`.

    :param arg_name: argument name for error message. Default - `"ids"`.
    """
    if iterable is None:
        return []
    _check_iterable_is_not_empty(iterable, arg_name=arg_name)
    return iterable


def _check_period_value(value: str) -> None | NoReturn:  # type: ignore[return]
    if value not in ('all_time', 'month'):
        raise BadArgumentsError(
            'the `period` arguments should be one of `\'all_time\'` and `\'month\'`,'
            f' but not `\'{value}\'`'
        )


def _check_access_token_and_app_key_are_passed(site: Any  # type: ignore[return]
                                               ) -> None | NoReturn:
    """
    Raises `AccessTokenOrAppKeyRequired` with message
    `access token and app key must be set.`,
    if one of attributes `access_token` and `app_key` of the `site` is `None`.

    :param site: instance of the `pystackapi.site.Site` class.
    """
    if site.access_token is None or site.app_key is None:
        raise AccessTokenOrAppKeyRequired('access token and app key must be set.')
