class DoublyLinkedDeque:

    class Node:

        def __init__(self, item, next=None, previous=None):
            self.item = item
            self.next = next
            self.previous = previous

    def __init__(self):
        self._front = None
        self._back = None

    def append_left(self, item):
        #self.front.previous = self.Node() # not that great
        new_node = self.Node(item, self._front)
        if self._front is not None:
            self._front.previous = new_node
        self._front = new_node

        if self._back is None:
            self._back = self._front

    def append(self, item):
        if self._front is None:
            self._front = self.Node(item)
            self._back = self._front
        else:
            #new_node = self.Node(item, None, self.back)
            new_node = self.Node(item, previous=self._back)
            self._back.next = new_node
            self._back = new_node

    # Best O(1)
    # Average O(1)
    # Worst O(1)
    def pop(self):
        self._check_for_empty()

        if self._front == self._back:
            item = self._front.item
            self._front = None
            self._back = None
            return item

        item = self._back.item
        self._back = self._back.previous
        self._back.next = None
        return item

    # Average O(1)
    # Worst O(1)
    def pop_left(self):
        self._check_for_empty()
        item = self._front.item
        self._front = self._front.next
        if self._front is None:
            self._back = None
        else:
            self._front.previous = None
        return item

    def front(self):
        self._check_for_empty()
        return self._front.item

    def back(self):
        self._check_for_empty()
        return self._back.item

    def _check_for_empty(self):
        if self._front is None:
            raise ValueError("Queue is empty")