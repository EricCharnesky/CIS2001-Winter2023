class CircularDoublyLinkedList:

    class Node:

        def __init__(self, item, next=None, previous=None):
            self.item = item
            self.next = next
            self.previous = previous

    def __init__(self):
        self._dummy_node = self.Node(None, None, None)
        self._dummy_node.next = self._dummy_node
        self._dummy_node.previous = self._dummy_node
        self._number_of_items = 0

    # Average O(1)
    # Worst O(1)
    def append(self, item):
        new_node = self.Node(item, next=self._dummy_node, previous=self._dummy_node.previous)
        new_node.previous.next = new_node
        new_node.next.previous = new_node
        self._number_of_items += 1

    # Average (n-k) k is the index
    def insert(self, index, item):
        if index < 0 or index > self._number_of_items:
            raise ValueError("Invalid index!")

        current_index = 0
        current_node = self._dummy_node.next

        while current_index < index:
            current_node = current_node.next
            current_index += 1

        new_node = self.Node(item, next=current_node, previous=current_node.previous)
        new_node.previous.next = new_node
        new_node.next.previous = new_node

        self._number_of_items += 1

    # O(n-k) k is the index
    # average time - O(n)
    # best time - O(1)
    # worst time - O(n)
    # todo - do this right
    def get(self, index):
        if index < 0 or index >= self._number_of_items:
            raise ValueError("Invalid index!")

        current_index = 0
        current_node = self._dummy_node.next

        while current_index < index:
            current_node = current_node.next
            current_index += 1

        return current_node.item

    # average time O(n-k) k is the index
    # best O(1) if it's the last or first
    def pop(self, index=None):
        if index is None:
            item = self._dummy_node.previous.item
            self._dummy_node.previous = self._dummy_node.previous.previous
            self._number_of_items -= 1
            return item

        if index < 0 or index >= self._number_of_items:
            raise ValueError("Invalid index!")

        current_index = 0
        current_node = self._dummy_node.next

        while current_index < index:
            current_node = current_node.next
            current_index += 1

        current_node.next.previous = current_node.previous
        current_node.previous.next = current_node.next

        self._number_of_items -= 1

        return current_node.item

    def __len__(self):
        return self._number_of_items


some_list = CircularDoublyLinkedList()

for number in range(5):
    some_list.append(number)

some_list.insert(0, -1)
some_list.insert(3, 1.5)
some_list.insert(7, 5)

print(some_list.pop(0))
print(some_list.pop(6))
print(some_list.pop(2))

for index in range(len(some_list)):
    print(some_list.get(index))