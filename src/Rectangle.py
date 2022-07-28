from src.Figure import Figure


class Rectangle(Figure):
    name = 'Rectangle'

    def get_perimeter(self, a, b):
        return 2 * a + 2 * b

    def get_area(self, a, b):
        return a * b

    def __init__(self, a, b):
        self.perimeter = self.get_perimeter(a, b)
        self.area = self.get_area(a, b)
