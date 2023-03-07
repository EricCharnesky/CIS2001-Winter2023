import random

from MaxPriorityQueue import MaxPriorityQueue

max_priority_queue = MaxPriorityQueue()

for value in range(100):
    max_priority_queue.add(random.randint(1, 1000))

while not max_priority_queue.is_empty():
    print(max_priority_queue.remove())





