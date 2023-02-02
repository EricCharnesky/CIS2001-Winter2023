class LinkedStack:

    class Node:

        def __init__(self, item, next=None):
            self.item = item
            self.next = next # really what come before it, or under it

    def __init__(self):
        self.top = None

    # Average O(1)
    # Worst O(1)
    def push(self, item):
        new_node = self.Node(item, self.top)
        self.top = new_node

    # Average O(1)
    # Worst O(1)
    def pop(self):
        self._check_for_empty()
        item = self.top.item
        self.top = self.top.next
        return item

    def _check_for_empty(self):
        if self.top is None:
            raise ValueError("Stack is empty")

    # Average O(1)
    # Worst O(1)
    def peek(self):
        self._check_for_empty()
        return self.top.item