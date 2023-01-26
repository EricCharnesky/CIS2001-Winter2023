from unittest import TestCase
from Cruiser import Cruiser
from Alignment import Alignment


class TestCruiser(TestCase):
    def test_move(self):
        expected_x = 1
        expected_y = 2
        expected_current_health = 41
        ship = Cruiser("", 0, 0, Alignment.US)
        ship.assess_damage(10)

        ship.move()
        actual_x = ship.get_x()
        actual_y = ship.get_y()
        actual_current_health = ship.get_current_health()

        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)
        self.assertEqual(expected_current_health, actual_current_health)

    def test_get_type(self):
        ship = Cruiser("", 0, 0, Alignment.US)
        expected_type = "Cruiser"

        actual_type = ship.get_type()

        self.assertEqual(expected_type, actual_type)
