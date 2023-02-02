from unittest import TestCase
from DoublyLinkedDeque import DoublyLinkedDeque


class TestDoublyLinkedDeque(TestCase):
    def test_append_left(self):
        # Arrange
        first_value = 5
        second_value = 7
        deque = DoublyLinkedDeque()

        # Act
        deque.append_left(second_value)
        deque.append_left(first_value)
        actual_first = deque.front()
        actual_second = deque.back()

        # Assert
        self.assertEqual(first_value, actual_first)
        self.assertEqual(second_value, actual_second)


    def test_append(self):
        # Arrange
        first_value = 5
        second_value = 7
        deque = DoublyLinkedDeque()

        # Act
        deque.append(first_value)
        deque.append(second_value)
        actual_first = deque.front()
        actual_second = deque.back()

        # Assert
        self.assertEqual(first_value, actual_first)
        self.assertEqual(second_value, actual_second)

    def test_pop(self):
        # Arrange
        first_value = 5
        second_value = 7
        deque = DoublyLinkedDeque()
        deque.append(first_value)
        deque.append(second_value)

        # Act
        actual_second = deque.pop()
        actual_first = deque.pop()

        # Assert
        self.assertEqual(first_value, actual_first)
        self.assertEqual(second_value, actual_second)

    def test_pop_left(self):
        # Arrange
        first_value = 5
        second_value = 7
        deque = DoublyLinkedDeque()
        deque.append(first_value)
        deque.append(second_value)

        # Act
        actual_first = deque.pop_left()
        actual_second = deque.pop_left()

        # Assert
        self.assertEqual(first_value, actual_first)
        self.assertEqual(second_value, actual_second)

    def test_add_empty_add_again(self):
        # Arrange
        first_value = 5
        second_value = 7
        deque = DoublyLinkedDeque()


        # Act
        deque.append(first_value)
        actual_first = deque.pop_left()
        deque.append(second_value)
        actual_second = deque.pop()

        # Assert
        self.assertEqual(first_value, actual_first)
        self.assertEqual(second_value, actual_second)
