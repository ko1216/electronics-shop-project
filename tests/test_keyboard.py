import pytest

from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('keyboard', 1000, 3)


def test_atribute(keyboard):
    assert keyboard.name == 'keyboard'
    assert keyboard.price == 1000
    assert keyboard.quantity == 3
    assert keyboard.language == 'EN'


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'
    keyboard.change_lang().change_lang()
    assert keyboard.language == 'EN'
