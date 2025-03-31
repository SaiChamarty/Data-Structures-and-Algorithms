# Implementation of Breadth First Search using a Queue data structure
# we can implement a queue by importing deque library and simulate first in first out functionality.

from collections import deque

# initialize the graph:
graph = {
    'A': ['B', 'G'],
    'B': ['C', 'D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['I'],
    'I': [],
}

start_node = 'A'
queue = deque()
queue.append(start_node)
visited = {start_node}
traversal_order = []

while len(queue) > 0:
    current_node = queue.popleft()
    traversal_order.append(current_node)
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)

print(f"Traversal order: {traversal_order}")
