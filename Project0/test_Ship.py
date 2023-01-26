from unittest import TestCase
from Alignment import Alignment
from Ship import Ship


class TestShip(TestCase):

    def test_init(self):
        # arrange
        expected_name = "some ship"
        expected_x = 1
        expected_y = 2
        expected_alignment = Alignment.US
        expected_max_health = 20
        expected_current_heath = 20
        expected_range = 25
        expected_attack_power = 10

        # act
        ship = Ship(expected_name, expected_x, expected_y, expected_alignment, expected_max_health, expected_range,
                    expected_attack_power)
        actual_name = ship.name
        actual_x = ship.get_x()
        actual_y = ship.get_y()
        actual_alignment = ship.get_alignment()
        actual_max_health = ship.get_max_health()
        actual_current_health = ship.get_current_health()
        actual_range = ship.get_range()
        actual_attack_power = ship.get_attack_power()

        # assert
        self.assertEqual(expected_name, actual_name)
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)
        self.assertEqual(expected_alignment, actual_alignment)
        self.assertEqual(expected_max_health, actual_max_health)
        self.assertEqual(expected_current_heath, actual_current_health)
        self.assertEqual(expected_range, actual_range)
        self.assertEqual(expected_attack_power, actual_attack_power)


    def test_assess_damage_doesnt_go_below_0(self):
        # arrange
        starting_health = 20
        expected_current_health = 0
        ship = Ship("", 0, 0, Alignment.US, starting_health, 0, 0)

        # act
        ship.assess_damage(starting_health*2)
        actual_current_health = ship.get_current_health()

        # assert
        self.assertEqual(expected_current_health, actual_current_health)

    def test_assess_damage_doesnt_go_above_max(self):
        # arrange
        expected_current_health = 20
        ship = Ship("", 0, 0, Alignment.US, expected_current_health, 0, 0)

        # act
        ship.assess_damage(-expected_current_health)
        actual_current_health = ship.get_current_health()

        # assert
        self.assertEqual(expected_current_health, actual_current_health)

    def test_move(self):
        # arrange
        expected_current_health = 11
        ship = Ship("", 0, 0, Alignment.US, 20, 0, 0)
        ship.assess_damage(10)

        # act
        ship.move()
        actual_current_health = ship.get_current_health()

        # assert
        self.assertEqual(expected_current_health, actual_current_health)

    def test_get_type(self):
        # arrange
        expected_type = "Ship"
        ship = Ship("", 0, 0, Alignment.US, 20, 0, 0)

        # act
        actual_type = ship.get_type()

        # assert
        self.assertEqual(expected_type, actual_type)

    def test_status(self):
        ship = Ship("ship name", 1, 2, Alignment.US, 20, 0, 0)
        expected_status = """ship name
type: Ship
health: 20
location: (1, 2)"""

        actual_status = ship.status()

        self.assertEqual(expected_status, actual_status)

    def test_change_alignment_us_to_them(self):
        expected_alignment = Alignment.THEM
        ship = Ship("ship name", 1, 2, Alignment.US, 20, 0, 0)

        ship.change_alignment()
        actual_alignment = ship.get_alignment()

        self.assertEqual(expected_alignment, actual_alignment)


    def test_change_alignment_them_to_us(self):
        expected_alignment = Alignment.US
        ship = Ship("ship name", 1, 2, Alignment.THEM, 20, 0, 0)

        ship.change_alignment()
        actual_alignment = ship.get_alignment()

        self.assertEqual(expected_alignment, actual_alignment)

    def test_change_alignment_chaotic_doesnt_change(self):
        expected_alignment = Alignment.CHAOTIC
        ship = Ship("ship name", 1, 2, Alignment.CHAOTIC, 20, 0, 0)

        ship.change_alignment()
        actual_alignment = ship.get_alignment()

        self.assertEqual(expected_alignment, actual_alignment)


    def test_attack_other_team_within_range(self):
        expected_target_current_health = 5
        ship = Ship("", 0, 0, Alignment.US, 10, 5, 5)
        target = Ship("", 1, 1, Alignment.THEM, 10, 5, 5)

        ship.attack(target)
        actual_target_current_health = target.get_current_health()

        self.assertEqual(expected_target_current_health, actual_target_current_health)

    def test_attack_chaotic_team_within_range(self):
        expected_target_current_health = 5
        ship = Ship("", 0, 0, Alignment.CHAOTIC, 10, 5, 5)
        target = Ship("", 1, 1, Alignment.CHAOTIC, 10, 5, 5)

        ship.attack(target)
        actual_target_current_health = target.get_current_health()

        self.assertEqual(expected_target_current_health, actual_target_current_health)

    def test_attack_chaotic_team_out_of_range(self):
        expected_target_current_health = 10
        ship = Ship("", 0, 0, Alignment.CHAOTIC, 10, 5, 5)
        target = Ship("", 5, 5, Alignment.CHAOTIC, 10, 5, 5)

        ship.attack(target)
        actual_target_current_health = target.get_current_health()

        self.assertEqual(expected_target_current_health, actual_target_current_health)
