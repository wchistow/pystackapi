"""Tests for model `User`."""
import lest

from pystackapi.models import User
from test_client import TestClient

client = TestClient()
user = User(client, {'account_id': 1})


@lest.register
def test_get_answers() -> None:
    user.get_answers()
    
    lest.assertions.assert_eq(client.query, f'users/{user.account_id}/answers')
    lest.assertions.assert_eq(client.kwargs, {})


@lest.register
def test_get_badges() -> None:
    user.get_badges()
    
    lest.assertions.assert_eq(client.query, f'users/{user.account_id}/badges')
    lest.assertions.assert_eq(client.kwargs, {})


@lest.register
def test_get_comments_without_toid() -> None:
    user.get_comments()
    
    lest.assertions.assert_eq(client.query, f'users/{user.account_id}/comments')
    lest.assertions.assert_eq(client.kwargs, {})


@lest.register
def test_get_comments_with_toid() -> None:
    user.get_comments(toid=1)

    lest.assertions.assert_eq(client.query, f'users/{user.account_id}/comments/1')
    lest.assertions.assert_eq(client.kwargs, {})


@lest.register
def test_get_privileges() -> None:
    user.get_privileges()

    lest.assertions.assert_eq(client.query, f'users/{user.account_id}/privileges')
    lest.assertions.assert_eq(client.kwargs, {})


@lest.register
def test_get_questions() -> None:
    user.get_questions()

    lest.assertions.assert_eq(client.query, f'users/{user.account_id}/questions')
    lest.assertions.assert_eq(client.kwargs, {})
