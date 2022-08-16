class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary search tree should be initialised as empty
class BinarySearchTree:
    def __init__(self):
        self.root = None

# Insert steps
# create a new node
# if root == None then root = new_node
# temp = self.root
# while loop
  # if new_node == temp return False
  # if < left else > right
  # if None insert new_node else move next
         
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
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
                
                
    def contains(self, value):
        temp = self.root
        
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        
    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
            
        return current_node.value
        
    def max_value_node(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
            
        return current_node.value    
            
my_tree = BinarySearchTree()
my_tree.insert(20)
my_tree.insert(10)
my_tree.insert(30)
my_tree.insert(32)
my_tree.insert(29)
my_tree.insert(-2)
# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
# print(my_tree.contains(1))

print(my_tree.min_value_node(my_tree.root))
print(my_tree.max_value_node(my_tree.root))

