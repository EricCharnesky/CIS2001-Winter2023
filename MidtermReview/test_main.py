from unittest import TestCase
from main import Burger

class TestBurger(TestCase):
    def test_get_total_cost(self):
        # arrange
        burger = Burger(1, 100, 100)
        expected_cost_in_cents = 200
        burger.set_actual_weight_in_grams(200)

        # act
        actual_cost_in_cents = burger.get_total_cost_in_cents()

        # assert
        self.assertEqual(expected_cost_in_cents, actual_cost_in_cents)
