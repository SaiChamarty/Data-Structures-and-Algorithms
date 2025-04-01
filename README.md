# Data-Structures-and-Algorithms
This repository consists of all the data structures and algorithms I learned and their example implementations in C++, Java and Python!
"C++ and Java are in progress"
Different algorithms and their pseudocodes are provided below.

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


# Prims Algorithm
Prims algorithm is used to find the Minimum Spanning Tree of a graph.
We use a priority queue here similar to Dijsktra!

## Time Complexity: O((V+E) log V)

## Pseudocode
```
# intialization
cost = {initialized to all infitities}
prev = {initialized to all zeros}
start_node

visited = {}

priority_queue = [(0, start_node)]

while priority_queue is not empty:
    current_cost, current_node = priority_queue.heappop()
    visited.add(current_node)
    for neighbors of current_node:
        if neighbor not yet visited:
            if cost[neighbor] > graph[current_node][neighbor]:
                cost[neighbor] = graph[current_node][neighbor]
                prev[neighbor] = current_node
                priority_queue.heappush((cost[neighbor], neighbor))
```

# Kruskal Algorithm
Kruskal algorithm is also used to find the Minimum Spanning Tree of a graph.
We use Union-Find data structure to implement this.

## Time Complexity: O(E log E)

## Pseudocode
```
graph = {}
MST

for each node in the graph:
    create a Union_Find set

def find(vertex):
    if vertex.parent == vertex:
        return vertex
    else:
        return find(vertex.parent)

def union(u,v):
    root_u = find(u)
    root_v = find(v)
    if root_u != root v:
        root_v.parent = root_u

sort all edges by weight

for all edges {u,v} in edges:
    if find(u) ≠ find(v):
        add edge {u, v} to MST
        Union(union_set(u),union_set(v))
```

# Dynamic Programming
Dynamic Programming is a method for solving complex problems by breaking them down into simpler, overlapping subproblems, solving each one once, and storing the results for reuse.

We can better understand the concept of DP by implementing the following problems:
1. Coin Changing Problem
2. Knapsack Problem
3. Seqence Alignment

## Coin Changing Problem
Given coin denominations D = {1, 3, 4} and a target value V = 6, use a dynamic programming approach to determine: <br />
1. The minimum number of coins needed to make change for 6.
2. One optimal set of coins that sums to 6

HINT: <br />
Define OPT(v) as the minimum number of coins needed to form the value v, with 
recurrence: <br />
    OPT(0) = 0, and for v > 0, <br />
    OPT(v) = min {OPT(v-d) + 1} for all coin denominations d such that v-d >= 0.

### Recursive Implementation of Coin Changing Problem:
#### Time Complexity: O(n * V)
In the recursive approach with memoization, each subproblem (each value from 0 to V, where V is the target) is solved once, and for each value, you iterate over all n coin denominations. Thus, the overall time complexity is O(n * V)
#### Psudocode:
```
D = [1, 3, 4]
target = 6
# we will create a memo dictionary to save the previously computed values of OPT
memo = {}

def OPT(v):
    # Base case:
    if v is 0, 
        return 0
    
    if v is already there in memo,
        return memo[v]
    
    minCoins = inf

    for each coin in D:
        if v-coin >= 0:
            result = OPT(v  - coin)
        
        if result is not inf:
            minCoins = min(minCoins, result + 1) # added one coin
    
    # we store the computed result in the memo so that we don't have to compute it again
    memo[v] = minCoins
    return minCoins

```

### Inplementation of Coin Changing using an Array:
#### Time Complexity: O(n * V)
The array (bottom-up) approach runs in O(n * V) time, where n is the number of coin denomitions, and V is the target value. Because for each subproblem 1 to V, we loop through each of the coin denominations (n) once.
#### Pseudocode
```
D = [1, 3, 4]
target = 6
OPT = [initialized to all infinities] * (target + 1)

## Base Case: (very important!!)
OPT[0] = 0

# loop through everything from 1 to target + 1
for v from 1 to target+1:
    # then loop through all coin denominations
    for coin in denominations:
        if v >= coin:
            OPT[v] = min(OPT[v], OPT(v-coin)+ 1) # save the min value
```

## Knapsack Problem
We will be given a maximum weight capacity and different items with weights and values. The problem is to find a way to pack the maximum total value into the knapsack without exceeding its weight capacity. We can also identify which items make up this optimal solution.

### Time Complexity: O(nW)
Where n is the number of items and W is the total weight capacity of the knapsack.

### Approach
```
1. Define the Subproblem
    Let dp[i][w] be the maximum value achievable with the first i items and a knapsack capacity of w.
2. Initialize a dp table (n+1) * (W+1)
    The table will have all 0's (if it applies), n+1 rows and W+1 columns.
3. Fill the dp table using recurrence relations below:
    For each item i (with weights w_i and value v_i) and capacity w:
        Case 1: Do not include item i.
            We do not include item i if its weight is more than the current capacity w
        Case 2: Include item i (w_i <= w):
            dp[i][w] = v_i + dp[i-1][w - w_i]
            Then we choose the max of the above two to fill in dp[i][w]
4. Traceback
    Now we traceback for finding the max values with the capacity. The idea is to start at the bottom right and work our way to top left, until i = 0 or w = 0.
    1. Start at the end dp[i][n]
    2. Compare current and previous rows:
        - if dp[i][w] == dp[i-1][w]:
            We did not include this item, so we skip it and not change w. But we reduce i by 1
        - if dp[i][w] != dp[i-1][w]
            We included this item. So we reduce w by w_i, and reduce i by 1. We also add the item's weight to optimal weight and record the item number in an array.
    3. Termination
        The loop will end, or the traceback terminates when there are no other rows to go up or w = 0, i.e., we reached the top left corner!
```