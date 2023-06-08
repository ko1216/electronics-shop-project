"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_table():
    return Item('table', 51.5, 10)


def test_item_calculate_total_price(item_table):
    assert item_table.calculate_total_price() == 515


def test_item_apply_discount(item_table):
    item_table.pay_rate = 0.8
    assert item_table.apply_discount() == 41.2
