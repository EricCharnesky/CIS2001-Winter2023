class Tree:

    def __init__(self, item=None, parent=None):
        self.parent = parent
        self.item = item
        self.children = []

    def add_child(self, item):
        self.children.append(Tree(item, self))

    def get_depth(self):
        if self.parent is None:
            return 0
        return 1 + self.parent.get_depth()

    def get_height(self):
        if self.is_leaf():
            return 0
        return 1 + max(child.get_height() for child in self.children)

    def get_height_bad(self):
        depths = []
        items = [self]
        while len(items) > 0:
            current_item = items.pop(0)  # this is bad should use a real queue
            for child in current_item.children:
                items.append(child)
            if current_item.is_leaf():
                depths.append(current_item.get_depth())
        return max(depths)

    def is_leaf(self):
        return len(self.children) == 0

    def get_child(self, index):
        return self.children[index]

    def print_tree_depth_first(self):
        print(self.item)
        for child in self.children:
            child.print_tree_depth_first()

    def print_tree_generation_by_generation(self):
        items = [self]
        while len(items) > 0:
            current_item = items.pop(0)  # this is bad should use a real queue
            for child in current_item.children:
                items.append(child)
            print(current_item.item)



trees = []

kingdom = Tree("Animalia")
trees.append(kingdom)
kingdom.add_child("Chordata")
chordata = kingdom.get_child(0)
trees.append(chordata)
chordata.add_child("Mammalia")
mammalia = chordata.get_child(0)
trees.append(mammalia)
mammalia.add_child("Carnivora")
mammalia.add_child("Rodentia")
mammalia.add_child("Primates")
carnivora = mammalia.get_child(0)
trees.append(carnivora)
carnivora.add_child("Felidae")
felidae = carnivora.get_child(0)
trees.append(felidae)
carnivora.add_child("Canidae")
canidae = carnivora.get_child(1)
trees.append(canidae)
rodentia = mammalia.get_child(1)
trees.append(rodentia)
rodentia.add_child("Sciuridae")
sciuridae = rodentia.get_child(0)
trees.append(sciuridae)
sciuridae.add_child("Marmota")
marmota = sciuridae.get_child(0)
trees.append(marmota)


kingdom.print_tree_depth_first()
kingdom.print_tree_generation_by_generation()

for tree in trees:
    print(f'{tree.item} has a depth of {tree.get_depth()} with a bad height of {tree.get_height_bad()} and a good height of {tree.get_height()}')