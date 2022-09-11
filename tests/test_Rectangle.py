import pytest
from src.Rectangle import Rectangle


@pytest.mark.parametrize("test_input, expected", [
    ((1, 1), 1),
    ((3, 2), 6),
    ((10, 3.1), 31)
])
def test_area(test_input, expected):
    obj = Rectangle(test_input[0], test_input[1])
    assert obj.area == expected


@pytest.mark.parametrize("test_input, expected", [
    ((1, 1), 4),
    ((3, 2), 10),
    ((10, 3.1), 26.2)
])
def test_perimeter(test_input, expected):
    obj = Rectangle(test_input[0], test_input[1])
    assert obj.perimeter == expected


def test_name():
    obj = Rectangle(1, 1)
    assert obj.name == 'Rectangle'