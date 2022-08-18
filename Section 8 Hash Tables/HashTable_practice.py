class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
        
    # O(1)    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, " :", val)
            
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    # Normal case O(1), as it fairly distributes the items
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map)):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def get_keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
                
        
            
my_hash_table = HashTable()
my_hash_table.set_item("boot", 123)
my_hash_table.set_item("apple", 111)
my_hash_table.set_item("hats", 89)

print(my_hash_table.get_keys())