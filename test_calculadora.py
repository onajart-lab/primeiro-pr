import pytest
from calculadora import soma, subtrai, multiplica, divide


def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0


def test_subtrai():
    assert subtrai(5, 3) == 2
    assert subtrai(0, 5) == -5
    assert subtrai(3, 3) == 0


def test_multiplica():
    assert multiplica(2, 4) == 8
    assert multiplica(-2, 3) == -6
    assert multiplica(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_por_zero():
    with pytest.raises(ValueError, match="Divisão por zero não é permitida"):
        divide(5, 0)
