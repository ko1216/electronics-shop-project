"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
import pytest


from src.item import Item, InstantiateCSVErrorException, InstantiateCSVError
from src.phone import Phone


@pytest.fixture
def item_table():
    return Item('стол', 51.5, 10)


@pytest.fixture
def phone_iphone():
    return Phone('Iphone', 100, 15, 2)


def test_item_calculate_total_price(item_table):
    assert item_table.calculate_total_price() == 515


def test_item_apply_discount(item_table):
    item_table.pay_rate = 0.8
    assert item_table.apply_discount() == 41.2


def test_name(item_table, phone_iphone):
    assert len(item_table.name) <= 10
    assert item_table.name == 'стол'
    item_table.name = 'dinner_table'
    assert item_table.name == 'dinner_tab...'
    item_table.name = 'столешница'
    assert item_table.name == 'столешница'
    assert phone_iphone.name == 'Iphone'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('1.1') == 1


def test_str(item_table):
    assert item_table.__str__() == 'стол'


def test_repr(item_table):
    assert item_table.__repr__() == "Item('стол', 51.5, 10)"


def test_add(item_table, phone_iphone):
    assert item_table + phone_iphone == 25


def test_instantiate_from_csv1():
    with pytest.raises(FileNotFoundError, match='Отсутствует файл item.csv'):
        file_path = 'test.csv'
        Item.instantiate_from_csv(file_path)


def test_instantiate_csv_error_class():
    with pytest.raises(InstantiateCSVErrorException):
        file_path = 'test_item.csv'

        with open(file_path, 'r', newline='', encoding='windows-1251') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            InstantiateCSVError(csv_reader)
