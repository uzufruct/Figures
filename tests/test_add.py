import pytest
import math
from src.Triangle import Triangle
from src.Circle import Circle
from src.Square import Square
from src.Rectangle import Rectangle


def test_add_negative():
    x = list
    obj = Circle(1)
    with pytest.raises(ValueError):
        obj.add_area(x)


@pytest.fixture()
def positive_test_data():
    square = Square(2)
    circle = Circle(1)
    rectangle = Rectangle(2, 3)
    triangle = Triangle(3, 4, 5)
    return ((square, circle), 4+math.pi), \
           ((rectangle, triangle), 12), \
           ((square, rectangle), 10)


def test_add_positive(positive_test_data):
    for test in positive_test_data:
        assert test[0][0].add_area(test[0][1]) == test[1]
