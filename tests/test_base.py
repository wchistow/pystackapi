"""Tests for base model."""
from typing import Any
import unittest

from pystackapi.models.base import BaseModel, SiteT
from test_client import TestClient


class _TestModel(BaseModel):
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(return_items=[{'id': 2}])
        self.base_model = BaseModel(self.client, {'id': 1})  # example data
    
    def test__get_call(self) -> None:
        """Tests for method `_get_call`."""
        result = self.base_model._get_call('some-url', _TestModel)

        self.assertEqual(len(result), 1)
        self.assertTrue(isinstance(result[0], _TestModel))
        self.assertEqual(result[0], _TestModel(self.client, {'id': 2}))
    
    def test_eq(self) -> None:
        """Tests for method `__eq__`."""
        other = BaseModel(self.client, {'id': 1})
        
        self.assertTrue(self.base_model == other)
    
    def test_getattr(self) -> None:
        """Tests for method `__getattr__`."""
        self.assertEqual(self.base_model.id, 1)
