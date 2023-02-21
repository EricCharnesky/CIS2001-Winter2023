# from text
class LinkedBinaryTree:

    class _Node:

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, position):
        if not isinstance(position, self.Position):
            raise TypeError
        if position._container is not self:
            raise ValueError("position does not belong to this container")
        if position._node._parent is position._node:
            raise ValueError("Position is no longer valid")
        return position._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self._make_position(self._root)

    def parent(self, position):
        node = self._validate(position)
        return self._make_position(node._parent)

    def num_children(self, position):
        node = self._validate(position)
        children = 0
        if node._left is not None:
            children += 1
        if node._right is not None:
            children += 1
        return children

    def __len__(self):
        return self._size

    def is_root(self, position):
        return self.root() == position

    def is_leaf(self, position):
        return self.num_children(position) == 0

    def is_empty(self):
        return len(self) == 0

    def left(self, position):
        node = self._validate(position)
        return self._make_position(node._left)

    def right(self, position):
        node = self._validate(position)
        return self._make_position(node._right)

    def sibling(self, position):
        parent = self.parent(position)
        if parent is None:
            return None
        if position == self.left(parent):
            return self.right(parent)
        return self.left(parent)

    def children(self, position):
        if self.left(position) is not None:
            yield self.left(position)
        if self.right(position) is not None:
            yield self.right(position)

    def add_root(self, element):
        if self._root is not None:
            raise ValueError("root already exists")
        self._size += 1
        self._root = self._Node(element)
        return self._make_position(self._root)

    def add_left(self, position, element):
        node = self._validate(position)
        if node._left is not None:
            raise ValueError("Position already has a left")
        self._size += 1
        node._left = self._Node(element, node)
        return self._make_position(node._left)

    def add_right(self, position, element):
        node = self._validate(position)
        if node._right is not None:
            raise ValueError("Position already has a left")
        self._size += 1
        node._right = self._Node(element, node)
        return self._make_position(node._right)

    def replace(self, position, element):
        node = self._validate(position)
        old_element = node._element
        node._element = element
        return old_element

    def delete(self, position):
        node = self._validate(position)
        if self.num_children(position) == 2:
            raise ValueError("Can not delete position with 2 children")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def depth(self, position):
        if self.is_root(position):
            return 0
        return 1 + self.depth(self.parent(position))

    def _height(self, position):
        if self.is_leaf(position):
            return 0
        return 1 + max(self._height(child) for child in self.children(position))

    def height(self, position=None):
        if position is None:
            position = self.root()
        return self._height(position)