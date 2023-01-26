from unittest import TestCase
from Battleship import Battleship
from Alignment import Alignment
from Ship import Ship


class TestBattleship(TestCase):
    def test_get_type(self):
        expected_type = "Battleship"
        ship = Battleship("", 0, 0, Alignment.US)

        actual_type = ship.get_type()

        self.assertEqual(expected_type, actual_type)

    def test_move(self):
        expected_x = -1
        expected_y = -1
        expected_current_health = 91
        ship = Battleship("", 0, 0, Alignment.US)
        ship.assess_damage(10)

        ship.move()
        actual_x = ship.get_x()
        actual_y = ship.get_y()
        actual_current_health = ship.get_current_health()

        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)
        self.assertEqual(expected_current_health, actual_current_health)

    def test_status(self):
        ship = Battleship("ship name", 1, 2, Alignment.US)
        expected_status = """ship name
type: Battleship
health: 100
location: (1, 2)
Torpedos: 10"""

        actual_status = ship.status()

        self.assertEqual(expected_status, actual_status)

    def test_attack(self):
        ship = Battleship("ship name", 1, 2, Alignment.US)
        target = Ship("ship name", 1, 2, Alignment.THEM, 250, 0, 0)
        expected_health_after_first_shot = 230
        expected_health_after_eleven_shots = 40
        expected_torpedos = 0

        ship.attack(target)
        actual_current_health_after_first_shot = target.get_current_health()
        for attack in range(10):
            ship.attack(target)
        actual_current_health_after_eleven_shots = target.get_current_health()
        actual_torpedos = ship.get_torpedos()

        self.assertEqual(expected_health_after_first_shot, actual_current_health_after_first_shot)
        self.assertEqual(expected_health_after_eleven_shots, actual_current_health_after_eleven_shots)
        self.assertEqual(expected_torpedos, actual_torpedos)


