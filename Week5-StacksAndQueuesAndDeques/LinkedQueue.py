class LinkedQueue:

    class Node:

        def __init__(self, item, next=None):
            self.item = item
            self.next = next

    def __init__(self):
        self.front = None
        self.back = None

    def front(self):
        self._check_for_empty()
        return self.front.item

    # Average O(1)
    # Worst O(1)
    def enqueue(self, item):
        if self.front is None:
            self.front = self.Node(item)
            self.back = self.front
        else:
            new_node = self.Node(item)
            self.back.next = new_node
            self.back = new_node

    # Average O(1)
    # Worst O(1)
    def dequeue(self):
        self._check_for_empty()
        item = self.front.item
        self.front = self.front.next
        if self.front is None:
            self.back = None
        return item

    def _check_for_empty(self):
        if self.front is None:
            raise ValueError("Queue is empty")