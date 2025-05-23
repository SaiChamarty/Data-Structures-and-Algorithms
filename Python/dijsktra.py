## test case from ChatGPT
import heapq

# create an adjacency list for showing a directed graph:

graph = {
    'A' : {'B': 2, 'C': 5}, # A is connected directing to B and C
    'B' : {'C': 1, 'D': 2}, # B is connected directing to C and D
    'C' : {'D': 3, 'E': 1}, # C is connected directing to D and E
    'D' : {'E': 2, 'F': 3}, # D is connected directing to E and F
    'E' : {'F': 2},         # E is connected directing only to F
    'F' : {}                # F is not directing to any other vertex
}

# lets initialize distance and previous dictionaries
dist = {}
prev = {}
start_node = 'A'
for u in graph:
    dist[u] = float('inf')
    prev[u] = None

# distance from A to A
dist['A'] = 0

H = [(0, start_node)] # a tuple with the current node and its distance from A

while H:
    # take the current node from the priority queue.
    current_distance, current_node = heapq.heappop(H)

    for vertex in graph[current_node]:
        if current_distance + graph[current_node][vertex] < dist[vertex]:
            dist[vertex] = current_distance + graph[current_node][vertex] # current distance + weight
            prev[vertex] = current_node
            heapq.heappush(H, (dist[vertex], vertex))




print(f"Intial distances: {dist}")
print(f"Initial previous nodes: {prev}")

