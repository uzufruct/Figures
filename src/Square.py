from src.Figure import Figure


class Square(Figure):
    name = 'Square'

    def __init__(self, a):
        self.area = self.get_area(a)
        self.perimeter = self.get_perimeter(a)

    def get_area(self, a):
        return a * a

    def get_perimeter(self, a):
        return 4 * a

