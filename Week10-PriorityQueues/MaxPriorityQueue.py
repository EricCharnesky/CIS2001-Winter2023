# chatgpt
# prompt - can you write a array based binary tree in python
# and adapted
class MaxPriorityQueue:
    def __init__(self):
        self._nodes = []

    def __len__(self):
        return len(self._nodes)

    def is_empty(self):
        return len(self._nodes) == 0

    def _upheap(self, index):
        parent_index = self._get_parent_index(index)
        if parent_index is not None and self._nodes[index] > self._nodes[parent_index]:
            # self.nodes[index], self.nodes[parent_index] = self.nodes[parent_index], self.nodes[index]
            temp = self._nodes[index]
            self._nodes[index] = self._nodes[parent_index]
            self._nodes[parent_index] = temp
            self._upheap(parent_index)

    def _downheap(self, index):
        largest_child_index = self._get_left_child_index(index)
        if largest_child_index is not None:
            right_child_index = self._get_right_child_index(index)
            if right_child_index is not None and self._nodes[right_child_index] > self._nodes[largest_child_index]:
                largest_child_index = right_child_index
            if self._nodes[index] < self._nodes[largest_child_index]:
                temp = self._nodes[index]
                self._nodes[index] = self._nodes[largest_child_index]
                self._nodes[largest_child_index] = temp
                self._downheap(largest_child_index)

    # average O ( log n )
    def add(self, value):
        self._nodes.append(value)
        self._upheap(len(self._nodes) - 1)

    # average O ( log n )
    def remove(self):
        if self.is_empty():
            raise ValueError("Priority Queue is empty!")
        if len(self._nodes) == 1:
            return self._nodes.pop()
        value = self._nodes[0]
        self._nodes[0] = self._nodes.pop()
        self._downheap(0)
        return value

    def get_max(self):
        return self._nodes[0]

    def _get_left_child_index(self, index):
        left_index = (2 * index) + 1
        if left_index < len(self._nodes):
            return left_index
        return None

    def _get_right_child_index(self, index):
        right_index = (2 * index) + 2
        if right_index < len(self._nodes):
            return right_index
        return None

    # chatgpt
    # can you add a function to get the parent's index
    def _get_parent_index(self, index):
        if index == 0:
            return None
        parent_index = (index - 1) // 2
        if parent_index < len(self._nodes):
            return parent_index
        return None