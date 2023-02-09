from unittest import TestCase
from main import CheckersSolver

class TestCheckersSolver(TestCase):

    def test_init_invalid_board_setup(self):

        # arrange
        board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'W', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'B', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        # act

        # assert
        with self.assertRaises(ValueError) as error:
            CheckersSolver(board)
        self.assertEqual("invalid board setup", str(error.exception))


    def test_get_max_jumps(self):

        # arrange
        board = [
            ['B', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'W', ' ', ' ', ' ', 'W', ' ', ' '],
            [' ', ' ', 'B', ' ', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', ' ', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', ' ', 'B', ' ', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        expected_max_jumps = 5

        # act
        checkersSolver = CheckersSolver(board)
        actual_max_jumps = checkersSolver.get_max_jumps()

        # assert
        self.assertEqual(expected_max_jumps, actual_max_jumps)

    def test_get_max_jumps_more(self):

        # arrange
        board = [
            ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'B', ' ', ' ', ' ', 'W', ' ', ' '],
            [' ', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', ' ', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', ' ', 'B', ' ', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        expected_max_jumps = 5

        # act
        checkersSolver = CheckersSolver(board)
        actual_max_jumps = checkersSolver.get_max_jumps()

        # assert
        self.assertEqual(expected_max_jumps, actual_max_jumps)
