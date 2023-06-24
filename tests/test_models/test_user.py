"""Tests for model `User`."""
import lest

from pystackapi.models import User
from patchs import ClientPatch

client = ClientPatch()
user = User(client, {'account_id': 1})


@lest.register
def test_get_answers() -> None:
    user.get_answers()
    
    lest.assert_eq(client.query, f'users/{user.account_id}/answers')
    lest.assert_eq(client.kwargs, {})


@lest.register
def test_get_badges() -> None:
    user.get_badges()
    
    lest.assert_eq(client.query, f'users/{user.account_id}/badges')
    lest.assert_eq(client.kwargs, {})


@lest.register
def test_get_comments_without_toid() -> None:
    user.get_comments()
    
    lest.assert_eq(client.query, f'users/{user.account_id}/comments')
    lest.assert_eq(client.kwargs, {})


@lest.register
def test_get_comments_with_toid() -> None:
    user.get_comments(toid=1)

    lest.assert_eq(client.query, f'users/{user.account_id}/comments/1')
    lest.assert_eq(client.kwargs, {})


@lest.register
def test_get_privileges() -> None:
    user.get_privileges()

    lest.assert_eq(client.query, f'users/{user.account_id}/privileges')
    lest.assert_eq(client.kwargs, {})


@lest.register
def test_get_questions() -> None:
    user.get_questions()

    lest.assert_eq(client.query, f'users/{user.account_id}/questions')
    lest.assert_eq(client.kwargs, {})
