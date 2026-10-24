import pytest
from calc import add, divide, multiply, parse_expression, subtract


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


def test_divide_by_zero():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        divide(6, 0)
