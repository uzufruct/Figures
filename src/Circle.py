from src.Figure import Figure
from math import pi


class Circle(Figure):
    name = 'Circle'

    def get_perimeter(self, r):
        return 2 * pi * r

    def get_area(self, r):
        return r * r * pi

    def __init__(self, r):
        self.perimeter = self.get_perimeter(r)
        self.area = self.get_area(r)
