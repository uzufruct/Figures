class Figure:
    name = 'Abstract Figure'
    area = 0
    perimeter = 0

    def add_area(self, second_figure):
        if isinstance(second_figure, Figure):
            return self.area + second_figure.area
        else:
            raise ValueError

    def __init__(self, params):
        pass
