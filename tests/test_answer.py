"""Tests for model `Answer`."""
import unittest

from pystackapi.models import Answer
from test_client import TestClient


class AnswerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient()
        self.answer = Answer(self.client, {'answer_id': 1})

    def test_get_comments(self) -> None:
        """Tests for method `get_comments`."""
        self.answer.get_comments()
        
        self.assertEqual(self.client.query, f'answers/{self.answer.answer_id}/comments')
        self.assertEqual(self.client.kwargs, {})
