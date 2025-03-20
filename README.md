# Data-Structures-and-Algorithms
This repository consists of all the data structures and algorithms I learned and their example implementations.

# Binary Search Algorithm
This algorithm is used to efficiently look up a particular item, for example a number, from an array which is sorted in ascending or descending order.

## Time Complexity: O(log n)
n is the length of the array being searched

## Pseudocode:
```
sortedArray = [...]
requiredNum = x
indexInArray = -1 # to be calculated if it exists

low = 0
high = len(sortedArray) - 1

while low <= high:
    mid = (low + high)/2
    if sortedArray[mid] > requiredNum:
        high = mid-1
    else if sortedArray[mid] < requriedNum:
        low = mid+1
    else:
        index = mid
        break
```

# Depth First Search
DFS searches a graph from the first node, to the deepest node first before searching adjacent nodes.
We use a stack data structure to perform this.

## Time Complexity
DFS has a time complexity of O(V+E), where
- V is the number of vertices.
- E is the number of edges.
This is because each vertex is processed once, and every edge is explored in the worst-case scenario.
We can say that the Time Complexity is O(n)

## Pseudocode:
```
graph = {}

node = initial_node
stack = []
visited = []
traversal_order = []

stack.push(node)

while stack not empty:
    current_node = stack.pop()
    visited(current_node)
    traversal_order.append(current_node)
    for neighbors of current_node:
        if neighbor not visited:
            stack.push(neighbor)
```

## Breadth First Search
BFS searches a graph from the first node, level by level. For performing this, we use a queue data structure to perform First In First Out functionality.

## Time Complexity
BFS has a time complexity of O(V+E), where
- V is the number of vertices.
- E is the number of edges.
This is because each vertex is processed once, and every edge is explored in the worst-case scenario.
We can say that the Time Complexity is O(n)

## Pseudocode
```
graph = {}
start_node
visited = {start_node}

queue = append(start_node)
traversal_order = []

while queue not empty:
    current_node = queue.pop()
    traversal_order.append(current_node)
    for neighbors of current_node:
        if neighbor not yet visited: 
            queue.push(neighbor)
            visited.add(neighbor)

traversal_order will have our BFS traversal, which will be level by level.
```

# Dijsktra's Algorithm
This algorithm is used to find the shortest path from one node to every other node in a directed or undirected graph with edge weights.

We can use a Priority Queue to implement this.
A Priority Queue is an abstract data type that allows you to store elements along with priorities. You can quickly retrieve (and often remove) the element with the highest (or lowest) priority.

In Dijsktra's algorithm, the priority queue is used to always select the next vertex with the smallest tentative distance.

## Time Complexity: O((V+E) log V)
This time complexity is when we use priority queue (using a binary heap) for retrieving and storing weights and edges. 

## Pseudocode:

```
start_node
dist = {initialized to all infinities} # shortest distance from starting node to every other node in the graph
prev = {initialized to all zeros} # keeps track of shortest path

priority_queue = [(0, start_node)] # is a tuple with initial weight and start_node

while priority_queue is not empty:
    current_weight, current_node = priority_queue.heappop()

    for neighbors of current_node:
        if current_weight + edge_weight[neighbor][current_node] < dist[neighbor]:
            dist[neighbor] = current_weight + edge_weight[neighbor][current_node]
            prev[neighbor] = current_node
            priority_queue.heappush((dist[neighbor], neighbor))

```

### Explanation
```dist``` dictionary stores the shortest distance from ```start_node``` to each node in the graph. <br />
```prev``` dictionary stores the previous node of each node in the shortest path. So this contains the shortest path.<br />
```priority_queue``` (implemented as a binary heap) stores tuples of the form (distance, node). Every time a node’s tentative distance is updated, it is pushed into the queue. When you pop from the queue, you get the node with the smallest tentative distance—the smallest sum of edge weights from the start_node to that node. This ensures that you process nodes in the order of increasing distance, so you don’t have to check all the edges repeatedly for each node, thus improving efficiency.<br />