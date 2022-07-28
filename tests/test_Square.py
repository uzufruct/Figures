import pytest
from src.Square import Square


@pytest.mark.parametrize("test_input, expected", [
    (1, 1),
    (3, 9),
    (10, 100)
])
def test_area(test_input, expected):
    obj = Square(test_input)
    assert obj.area == expected


@pytest.mark.parametrize("test_input, expected", [
    (1, 4),
    (3, 12),
    (10, 40)
])
def test_perimeter(test_input, expected):
    obj = Square(test_input)
    assert obj.perimeter == expected


def test_name():
    obj = Square(1)
    assert obj.name == 'Square'
