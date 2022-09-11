import pytest
from src.Triangle import Triangle
import math


def test_init_negative():
    with pytest.raises(ValueError):
        Triangle(18, 1, 2)


def test_init_positive():
    Triangle(3, 4, 5)


@pytest.mark.parametrize("test_input, expected", [
    ((1, 1, 1), 0.25 * math.sqrt(3.0)),
    ((3, 4, 5), 6),
    ((5, 5, 6), 12)
])
def test_area(test_input, expected):
    obj = Triangle(test_input[0], test_input[1], test_input[2])
    assert obj.area == expected


@pytest.mark.parametrize("test_input, expected", [
    ((1, 1, 1), 3),
    ((3, 4, 5), 12),
    ((5, 5, 6), 16)
])
def test_perimeter(test_input, expected):
    obj = Triangle(test_input[0], test_input[1], test_input[2])
    assert obj.perimeter == expected


def test_name():
    obj = Triangle(1, 1, 1)
    assert obj.name == 'Triangle'