import pytest
from src.Triangle import Triangle
from src.Circle import Circle
from src.Square import Square
from src.Rectangle import Rectangle


def test_add_negative():
    x = list
    obj = Circle(1)
    with pytest.raises(ValueError):
        obj.add_area(x)


