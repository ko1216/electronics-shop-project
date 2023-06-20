import pytest

from src.phone import Phone


@pytest.fixture
def phone_iphone():
    return Phone('iPhone 14', 120000, 5, 2)


def test_number_of_sim(phone_iphone):
    assert phone_iphone.number_of_sim == 2


def test_repr(phone_iphone):
    assert repr(phone_iphone) == "Phone('iPhone 14', 120000, 5, 2)"
