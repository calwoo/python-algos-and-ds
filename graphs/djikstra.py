from graph import Graph

# build graph
graph = Graph()
graph.add_vertex("start")
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_edge("start", "A", cost=6)
graph.add_edge("start", "B", cost=2)
graph.add_edge("B", "A", cost=3)
graph.add_edge("A", "fin", cost=1)
graph.add_edge("B", "fin", cost=5)

# print out graph details
for vertex in graph.get_vertices():
    print(graph.get_vertex(vertex))