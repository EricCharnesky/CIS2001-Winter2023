class SinglyLinkedDeque:

    class Node:

        def __init__(self, item, next=None):
            self.item = item
            self.next = next

    def __init__(self):
        self.front = None
        self.back = None

    def append_left(self, item):
        new_node = self.Node(item, self.front)
        self.front = new_node
        if self.back is None:
            self.back = self.front

    def append(self, item):
        if self.front is None:
            self.front = self.Node(item)
            self.back = self.front
        else:
            new_node = self.Node(item)
            self.back.next = new_node
            self.back = new_node

    # Best O(N)
    # Average O(N)
    # Worst O(n)
    def pop(self):
        self._check_for_empty()

        if self.front == self.back:
            item = self.front.item
            self.front = None
            self.back = None
            return item

        current_node = self.front
        while current_node.next != self.back:
            current_node = current_node.next
        item = self.back.item
        self.back = current_node

    # Average O(1)
    # Worst O(1)
    def pop_left(self):
        self._check_for_empty()
        item = self.front.item
        self.front = self.front.next
        if self.front is None:
            self.back = None
        return item

    def front(self):
        self._check_for_empty()
        return self.front.item

    def back(self):
        self._check_for_empty()
        return self.back.item

    def _check_for_empty(self):
        if self.front is None:
            raise ValueError("Queue is empty")