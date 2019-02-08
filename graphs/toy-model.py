# simply describe graph as a hash table
graph = {}
graph["start"] = {"A":6, "B":2}
graph["A"] = {"fin":1}
graph["B"] = {"A":3, "fin":5}
graph["fin"] = {}

infinity = float("inf")

# get a hash table of costs to each node
costs = {}
