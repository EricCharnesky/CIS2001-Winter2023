from Ship import Ship
from Alignment import Alignment


class Cruiser(Ship):

    def __init__(self, name, x, y, alignment):
        super().__init__(name, x, y, alignment, 50, 50, 5)

    def move(self):
        super().move()
        self._x_location += 1
        self._y_location += 2

    def get_type(self):
        return "Cruiser"