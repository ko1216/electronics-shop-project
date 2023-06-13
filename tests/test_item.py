"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_table():
    return Item('стол', 51.5, 10)


def test_item_calculate_total_price(item_table):
    assert item_table.calculate_total_price() == 515


def test_item_apply_discount(item_table):
    item_table.pay_rate = 0.8
    assert item_table.apply_discount() == 41.2


def test_name(item_table):
    assert len(item_table.name) <= 10
    assert item_table.name == 'стол'
    item_table.name = 'dinner_table'
    assert item_table.name == 'dinner_tab...'
    item_table.name = 'столешница'
    assert item_table.name == 'столешница'

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 8

def test_string_to_number():
    assert Item.string_to_number('1.1') == 1
