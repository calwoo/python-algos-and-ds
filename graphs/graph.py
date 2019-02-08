"""
Implementation of a graph data structure as an adjacency list.
"""

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def __str__(self):
        return str(self.key) + " is connected to: " + str([v.key for v in self.neighbors])
    
    def get_neighbors(self):
        return self.neighbors.keys()

    def get_key(self):
        return self.key

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        new = Vertex(key)
        self.vertices[key] = new
        self.num_vertices += 1
        return new

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def add_edge(self, begin, end, cost=0):
        if begin not in self.vertices:
            _ = self.add_vertex(begin)
        if end not in self.vertices:
            _ = self.add_vertex(end)
        self.vertices[begin].add_neighbor(self.vertices[end], cost)

    def get_vertices(self):
        return self.vertices.keys()


