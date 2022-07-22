from hashlib import new


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
        
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp
            
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        else:
            return False
        
        
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index-1)
        after = self.get(index)
        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
        
        self.length += 1
        return True
    
    
    def remove(self, index):
        if index <0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = temp.next
        after.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
    # My method (I wrote it)
    # def remove(self, index):
    #     if index < 0 or index >= self.length:
    #         return False
    #     if index == 0:
    #         return self.pop_first
    #     if index == self.length -1:
    #         return self.pop
        
    #     temp = self.get(index)
    #     before = temp.prev
    #     after = temp.next
    #     before.next = after
    #     after.prev = before
    #     temp.next = None
    #     temp.prev = None
    #     self.length -= 1
    #     return temp
 
        
        
my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.remove(1)
my_doubly_linked_list.print_list()
