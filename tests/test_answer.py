"""Tests for model `Answer`."""
import lest

from pystackapi.models import Answer
from test_client import TestClient

client = TestClient()
answer = Answer(client, {'answer_id': 1})


@lest.register
def test_get_comments() -> None:
    """Tests for method `get_comments`."""
    answer.get_comments()

    lest.assertions.assert_eq(client.query, f'answers/{answer.answer_id}/comments')
    lest.assertions.assert_eq(client.kwargs, {})
