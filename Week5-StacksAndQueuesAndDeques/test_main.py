from unittest import TestCase
from main import CircularQueue

class TestCircularQueue(TestCase):
    def test_enqueue(self):
        #arange?
        queue = CircularQueue()

        #act
        for number in range(50):
            queue.enqueue(number)

        # asserting
        for number in range(50):
            self.assertEqual(number, queue.dequeue())





    def test_front(self):
        self.fail()
