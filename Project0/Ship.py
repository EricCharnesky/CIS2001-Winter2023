from Alignment import Alignment
import math


class Ship:

    def __init__(self, name, x, y, alignment, max_health, range, attack_power):
        self.name = name
        self._x_location = x
        self._y_location = y
        self._alignment = alignment
        self._max_health = max_health
        self._current_health = max_health
        self._range = range
        self._attack_power = attack_power

    def get_x(self):
        return self._x_location

    def get_y(self):
        return self._y_location

    def get_max_health(self):
        return self._max_health

    def get_current_health(self):
        return self._current_health

    def get_range(self):
        return self._range

    def get_attack_power(self):
        return self._attack_power

    def get_alignment(self):
        return self._alignment

    def _is_target_within_range(self, target):
        return math.sqrt((self._x_location - target.get_x())**2 +
        (self._y_location - target.get_y())**2) <= self._range

    def assess_damage(self, amount):
        self._current_health -= amount
        if self._current_health < 0:
            self._current_health = 0
        elif self._current_health > self._max_health:
            self._current_health = self._max_health

    def move(self):
        self.assess_damage(-1)

    def get_type(self):
        return "Ship"

    def status(self):
        return f"{self.name}\n" \
            + f"type: {self.get_type()}\n" \
            + f"health: {self._current_health}\n" \
            + f"location: ({self.get_x()}, {self.get_y()})"

    def change_alignment(self):
        if self._alignment == Alignment.US:
            self._alignment = Alignment.THEM
        elif self._alignment == Alignment.THEM:
            self._alignment = Alignment.US

    def _should_attack(self, target):
        return self._alignment == Alignment.CHAOTIC or \
                self._alignment != target.get_alignment()

    def attack(self, target):
        if self._should_attack(target) and self._is_target_within_range(target):
            target.assess_damage(self._attack_power)
