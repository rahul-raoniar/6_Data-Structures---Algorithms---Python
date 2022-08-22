# Graph has Vertex or Nodes
# It has Edge or Connection
# The Edge strength can be stored in Adjacency Matrix or List

####################################
# Big (O)
####################################
# Space Complexcity
# For adjacency list --> O(|V|+|E|)
# For adjacency martix --> O(|V|2)

####################################
# Time Complexicity
# Adding a vertex --> 
# For adjacency list --> O(1)
# For adjacency martix --> O(|V|2) it is rewriting the entire matrix

# Adding a edge --> 
# For adjacency list --> O(1)
# For adjacency martix --> O(1)

# Removing a edge --> 
# For adjacency list --> O(E)
# For adjacency martix --> O(1)

# Removing a vertex --> 
# For adjacency list --> O(|V|+|E|)
# For adjacency martix --> O(|V2|)

class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
            
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_edge(1, 2)
my_graph.print_graph()