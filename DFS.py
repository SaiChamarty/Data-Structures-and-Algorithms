# here, we will implement depth first search algorithm using a stack data structure
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

# we start dfs on node and traverse through the graph
def dfs(graph, node):
    traversal_path = []
    visited = [] # important for cyclic graphs, but not for acyclic graphs like this
    stack = deque()
    stack.appendleft(node)
    while len(stack) > 0:
        curr_node = stack.popleft() # pop the top of the stack 
        traversal_path.append(curr_node)
        visited.append(curr_node) # not being used here...
        for neighbor in graph[curr_node]:
            stack.appendleft(neighbor)
    
    return traversal_path

node = 'A'
traversal_path = dfs(graph, node)
print(f"Traversal path by Depth First Search is: {traversal_path}")    
