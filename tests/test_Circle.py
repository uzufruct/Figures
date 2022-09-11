from src.Circle import Circle
import math
import pytest


@pytest.mark.parametrize("test_input, expected", [
    (1, math.pi),
    (2, 4 * math.pi),
    (10, 100 * math.pi)
])
def test_area(test_input, expected):
    obj = Circle(test_input)
    assert obj.area == expected


@pytest.mark.parametrize("test_input, expected", [
    (1, 2 * math.pi),
    (2, 4 * math.pi),
    (10, 20 * math.pi)
])
def test_perimeter(test_input, expected):
    obj = Circle(test_input)
    assert obj.perimeter == expected


def test_name():
    obj = Circle(1)
    assert obj.name == 'Circle'
