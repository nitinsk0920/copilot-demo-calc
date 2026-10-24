import pytest

from calc import add, average, divide, multiply, parse_expression, subtract


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(3, 1) == 2


def test_multiply():
    assert multiply(2, 4) == 8


def test_divide():
    assert divide(6, 3) == 2


def test_parse_expression():
    assert parse_expression("6 / 3") == 2


def test_average():
    assert average([2, 4, 6]) == 4
    assert average([1.5, 2.5]) == 2


def test_average_empty_list():
    with pytest.raises(ValueError, match="cannot average an empty list"):
        average([])
