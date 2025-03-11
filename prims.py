import heapq
# implementation of Prim Algorithm for finding the Minimum Spanning Tree

# we need an undirected connected graph, but for testing purposes, we are going to use a fully connected graph

## Algorithm Procedure/ Pseudocode:
# Input: A connected undirected graph G=(Vertices, Edges)

# Fully connected undirected graph for Prim's algorithm testing
graph = {
    'A': {'B': 2, 'C': 3, 'D': 6, 'E': 8},
    'B': {'A': 2, 'C': 5, 'D': 7, 'E': 9},
    'C': {'A': 3, 'B': 5, 'D': 4, 'E': 6},
    'D': {'A': 6, 'B': 7, 'C': 4, 'E': 2},
    'E': {'A': 8, 'B': 9, 'C': 6, 'D': 2}
}

# Output: A minimum spanning tree defined by the array prev

cost = {} # dictionary for min costs to each of the vertices
prev = {} # keeping track of the minimum spannning tree
visited = {} # keeping track of visited nodes

for u in graph:
    cost[u] = float('inf')
    prev[u] = None
    visited[u] = False

# Pick any initial vertex/node: 'A'
start_node = 'A'
cost[start_node] = 0

H = [(0, start_node)]

while H:
    current_cost, current_node = heapq.heappop(H)
    visited[current_node] = True
    for node in graph[current_node]:
        if not visited[node]:
            if cost[node] > graph[current_node][node]:
                cost[node] = graph[current_node][node]
                prev[node] = current_node
                heapq.heappush(H, (cost[node], node))


# print out the output:
print(f"Minimum spanning tree: {prev}")
print(f"Minimum spanning tree costs: {cost}")
print(f"Total edge weight: {sum(cost.values())}")