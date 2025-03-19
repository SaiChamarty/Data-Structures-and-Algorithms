# Data-Structures-and-Algorithms
This repository consists of all the data structures and algorithms I learned and their example implementations.

# Binary Search Algorithm
This algorithm is used to efficiently look up a particular item, for example a number, from an array which is sorted in ascending or descending order.

## Time Complexity: O(log n)
n is the length of the array being searched

## Pseudocode:
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
