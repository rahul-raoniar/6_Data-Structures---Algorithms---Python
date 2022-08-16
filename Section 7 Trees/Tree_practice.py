class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return None
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
my_binary_tree = BinaryTree()
my_binary_tree.insert(12)
my_binary_tree.insert(10)
my_binary_tree.insert(14)
my_binary_tree.insert(5)
print("root:", my_binary_tree.root.value)
print("left:", my_binary_tree.root.left.value)
print("right:", my_binary_tree.root.right.value)
print(my_binary_tree.root.left.left.value)