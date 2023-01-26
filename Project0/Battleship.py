from Ship import Ship
from Alignment import Alignment


class Battleship(Ship):

    def __init__(self, name, x, y, alignment):
        super().__init__(name, x, y, alignment, 100, 10, 10)
        self._torpedos = 10

    def get_type(self):
        return "Battleship"

    def move(self):
        super().move()
        self._x_location -= 1
        self._y_location -= 1

    def status(self):
        return super().status() + f"\nTorpedos: {self._torpedos}"

    def attack(self, target):
        if self._should_attack(target) and self._is_target_within_range(target):
            damage = self.get_attack_power()
            if self._torpedos > 0:
                damage += 10
                self._torpedos -= 1
            target.assess_damage(damage)

    def get_torpedos(self):
        return self._torpedos
