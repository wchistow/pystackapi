"""Tests for base model."""
from typing import Any

import lest

from pystackapi.models.base import BaseModel, SiteT
from test_client import TestClient

test_client = TestClient(return_items=[{'id': 2}])
base_model = BaseModel(test_client, {'id': 1})  # example data


class _TestModel(BaseModel):
    def __init__(self, client: SiteT, data: dict[Any, Any]) -> None:
        super().__init__(client, data)


@lest.register
def test__get_call() -> None:
    """Tests for method `_get_call`."""
    result = base_model._get_call('some-url', _TestModel)

    lest.assert_eq(len(result), 1)
    lest.assert_true(isinstance(result[0], _TestModel))
    lest.assert_eq(result[0], _TestModel(test_client, {'id': 2}))


@lest.register
def test_eq() -> None:
    """Tests for method `__eq__`."""
    other = BaseModel(test_client, {'id': 1})

    lest.assert_true(base_model == other)


@lest.register
def test_getattr() -> None:
    """Tests for method `__getattr__`."""
    lest.assert_eq(base_model.id, 1)
