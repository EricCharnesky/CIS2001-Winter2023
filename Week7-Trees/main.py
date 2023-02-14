class Tree:

    def __init__(self, item=None):
        self.item = item
        self.children = []

    def add_child(self, item):
        self.children.append(Tree(item))

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


kingdom = Tree("Animalia")
kingdom.add_child("Chordata")
chordata = kingdom.get_child(0)
chordata.add_child("Mammalia")
mammalia = chordata.get_child(0)
mammalia.add_child("Carnivora")
mammalia.add_child("Rodentia")
mammalia.add_child("Primates")
carnivora = mammalia.get_child(0)
carnivora.add_child("Felidae")
carnivora.add_child("Canidae")
rodentia = mammalia.get_child(1)
rodentia.add_child("Sciuridae")
sciuridae = rodentia.get_child(0)
sciuridae.add_child("Marmota")


kingdom.print_tree_depth_first()
kingdom.print_tree_generation_by_generation()

