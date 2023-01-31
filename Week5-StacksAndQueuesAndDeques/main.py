
#Stack - First In Last Out

#Queue - First In First Out

class Stack:

    def __init__(self):
        self.storage = []

    # average - O(1)
    # worst - O(n)
    def push(self, item):
        self.storage.append(item)

    # average - O(1)
    # worst - O(n)
    def pop(self):
        return self.storage.pop()

    # average - O(1)
    # worst - O(1)
    def peek(self):
        return self.storage[-1]
        #return self.storage[len(self.storage) - 1]


class Queue:

    def __init__(self):
        self.storage = []

    # average - O(1)
    # worst - O(n)
    def enqueue(self, item):
        self.storage.append(item)

    # average - O(n)
    # worst - O(n)
    def dequeue(self):
        return self.storage.pop(0)

    # average - O(1)
    # worst - O(1)
    def front(self):
        return self.storage[0]


class Deque:

    def __init__(self):
        self.storage = []

    # average O(n)
    # worst O(n)
    def append_left(self, item):
        self.storage.insert(0, item)

    # average - O(1)
    # worst - O(n)
    def append(self, item):
        self.storage.append(item)

    # average - O(1)
    # worst - O(n)
    def pop(self):
        return self.storage.pop()

    # average - O(n)
    # worst - O(n)
    def pop_left(self):
        return self.storage.pop(0)

    # average - O(1)
    # worst - O(1)
    def front(self):
        return self.storage[0]

    # average - O(1)
    # worst - O(1)
    def back(self):
        return self.storage[-1]


class CircularQueue:

    def __init__(self):
        self._storage = [None] * 5
        self._front_index = 0
        self._number_of_items = 0

    def _resize(self):
        new_storage = [None] * (len(self._storage) * 2)
        new_storage_current_index = 0

        for index in range(self._front_index, len(self._storage)):
            new_storage[new_storage_current_index] = self._storage[index]
            new_storage_current_index += 1

        for index in range(0, self._front_index):
            new_storage[new_storage_current_index] = self._storage[index]
            new_storage_current_index += 1

        self._storage = new_storage
        self._front_index = 0

    # average - O(1)
    # worst - O(n)
    def enqueue(self, item):
        if self._number_of_items == len(self._storage):
            self._resize() # will come back to
        self._storage[(self._front_index+self._number_of_items) % len(self._storage)] = item
        self._number_of_items += 1
    # average - O(1)
    # worst - O(1) - bad for memory
    def dequeue(self):
        item = self._storage[self._front_index]
        self._storage[self._front_index] = None
        self._front_index = (self._front_index + 1) % len(self._storage)
        self._number_of_items -= 1
        return item

    # average - O(1)
    # worst - O(1)
    def front(self):
        return self._storage[self._front_index]
