"""
Breadth-first search
    INPUT
        directed graph, start, endpoint
    OUTPUT
        shortest path from start to end
"""

# dumb graph implementation
graph = {} # represent a graph as a hash table
# for example, a -> b is represented by
graph["a"] = ["b"]

from collections import deque

# this is a terrible and naive version of bfs
def bfs(graph, begin, end):
    queue = deque()
    queue.append(begin)
    while len(queue) != 0:
        popped = queue.pop()
        if popped == end:
            return "found it"
        for item in graph[popped]:
            queue.append(item)
    return "can't find"
        