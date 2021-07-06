class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def get_nodes(self):
        return list(self.adjacency_list.keys())

    def size(self):
        return len(self.adjacency_list)

    def add_edge(self, start_v, end_v, weight=0):
        edge = Edge(end_v, weight)
        self.adjacency_list[start_v].append(edge)

    def get_neighbors(self,vertex):
        return self.adjacency_list[vertex]
    
class Vertex:
    def __init__(self, value) -> None:
        self.value = value

class Edge:
    def __init__(self, vertex, weight) -> None:
        self.vertex = vertex
        self.weight = weight
