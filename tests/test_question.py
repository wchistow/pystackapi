"""Tests for model `Question`."""
import lest

from pystackapi.models import Question
from test_client import TestClient

client = TestClient()
question = Question(client, {'question_id': 1})


@lest.register
def test_get_answers() -> None:
    question.get_answers()
    
    lest.assert_eq(client.query, f'questions/{question.question_id}/answers')
    lest.assert_eq(client.kwargs, {})


@lest.register
def test_get_comments() -> None:
    question.get_comments()

    lest.assert_eq(client.query, f'questions/{question.question_id}/comments')
    lest.assert_eq(client.kwargs, {})
