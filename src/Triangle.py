from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    name = 'Triangle'

    @staticmethod
    def check_triangle(a, b, c):
        if (a + b > c) and (a + c > b) and (b + c > a):
            return True
        else:
            return False

    def get_area(self, a, b, c):
        p = self.perimeter / 2.0
        pa = p - a
        pb = p - b
        pc = p - c
        return sqrt(p * pa * pb * pc)

    @staticmethod
    def get_perimeter(a, b, c):
        return a + b + c

    def __init__(self, a, b, c):
        if self.check_triangle(a, b, c):
            self.perimeter = self.get_perimeter(a, b, c)
            self.area = self.get_area(a, b, c)
        else:
            raise ValueError
