# simply describe graph as a hash table
graph = {}
graph["start"] = {"A":6, "B":2}
graph["A"] = {"fin":1}
graph["B"] = {"A":3, "fin":5}
graph["fin"] = {}

infinity = float("inf")

# get a hash table of costs to each node
costs = {"A":6, "B":2, "fin":infinity}

# hash table for parents
parents = {"A": "start", "B": "start", "fin": None}

# need a list to store nodes we've already visited
visited = []

## helper function -- find lowest cost node
def lc_node(costs):
    lowest = float("inf")
    lowest_node = None
    for node in costs:
        if costs[node] < lowest and node not in visited:
            lowest = costs[node]
            lowest_node = node
    return lowest_node

# djikstra's algorithm
node = lc_node(costs) # first, grab the lowest node in all of the graph
while node is not None: # we keep going until we've seen all the nodes
    cost = costs[node]
    neighbors = graph[node]
    for nb in neighbors.keys():
        new_cost = cost + neighbors[nb]
        if new_cost < costs[nb]:
            # the cost of a node is the lowest cost across all paths
            costs[nb] = new_cost
            # new parent of neighbor node. this allows us to backtrack
            parents[nb] = node 
    # when done with neighbors, we've processed the node, so add to visited
    visited.append(node)
    node = lc_node(costs)

def lc_path(parents):
    node = "fin"
    path = ["fin"]
    while True:
        path.append(parents[node])
        if parents[node] == "start":
            break
        else:
            node = parents[node]
    path.reverse()
    return path

print(lc_path(parents))
