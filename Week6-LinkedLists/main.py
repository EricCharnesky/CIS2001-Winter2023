class DoublyLinkedList:

    class Node:

        def __init__(self, item, next=None, previous=None):
            self.item = item
            self.next = next
            self.previous = previous

    def __init__(self):
        self._front = None
        self._back = None
        self._number_of_items = 0

    def append(self, item):
        new_node = self.Node(item, next=None, previous=self._back)
        if new_node.previous is None:
            self._front = new_node
        else:
            self._back.next = new_node

        self._back = new_node
        self._number_of_items += 1

    def insert(self, index, item):
        if index < 0 or index > self._number_of_items:
            raise ValueError("Invalid index!")
        if index == self._number_of_items:
            self.append(item)
            return

        current_index = 0
        current_node = self._front

        while current_index < index:
            current_node = current_node.next
            current_index += 1

        new_node = self.Node(item, next=current_node, previous=current_node.previous)
        if new_node.previous is not None:
            new_node.previous.next = new_node
        else:
            self._front = new_node

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
        current_node = self._front

        while current_index < index:
            current_node = current_node.next
            current_index += 1

        return current_node.item


    def pop(self, index=None):
        if index is None:
            item = self._back.item
            self._back = self._back.previous
            if self._back is not None:
                self._back.next = None
            else:
                self._front = None
            self._number_of_items -= 1
            return item

        if index < 0 or index >= self._number_of_items:
            raise ValueError("Invalid index!")

        if index == self._number_of_items - 1:
            return self.pop()

        current_index = 0
        current_node = self._front

        while current_index < index:
            current_node = current_node.next
            current_index += 1

        current_node.next.previous = current_node.previous
        if current_node.previous is not None:
            current_node.previous.next = current_node.next
        else:
            self._front = current_node.next

        self._number_of_items -= 1

        return current_node.item

    def __len__(self):
        return self._number_of_items


some_list = DoublyLinkedList()

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
