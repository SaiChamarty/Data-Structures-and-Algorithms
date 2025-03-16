# Implementation of kruskal algorithm to find MST for the following graph. 
# MST has been found/ solved using prims in prims.py

'''
We solve this problem using Union Find data structure. 
Kruskal algorithm will keep track of individual edges that do not create a cycle of edges. 
It starts with the smallest connected edge and keeps adding connected edges until all vertices are in the tree.
Union function merges two un-connected trees into one. One parent is selected.
Find function finds the head of each tree, i.e. the parent of each tree.
'''

graph = {
    'A': {'B': 2, 'C': 3, 'D': 6, 'E': 8},
    'B': {'A': 2, 'C': 5, 'D': 7, 'E': 9},
    'C': {'A': 3, 'B': 5, 'D': 4, 'E': 6},
    'D': {'A': 6, 'B': 7, 'C': 4, 'E': 2},
    'E': {'A': 8, 'B': 9, 'C': 6, 'D': 2}
}

# Time Complexity: O(E log E)

class UnionSet:
    def __init__(self):
        self.parent = self
        self.rank = 0
    
    # find function that returns the parent of the UnionSet, which is the tree
    def find(self):
        if self.parent == self:
            return self
        else:
            self.parent = self.parent.find()
            return self.parent
    
    # add a vertex and an edge to this tree
    def union(self, other: "UnionSet"):
        rootX = self.find()
        rootY = other.find()

        if rootX != rootY:
            if rootX.rank > rootY.rank:
                rootY.parent = rootX
            elif rootX.rank < rootY.rank:
                rootX.parent = rootY
            else:
                rootY.parent = rootX
                rootX.rank += 1

# Initialize Union-Find for each vertex
sets = {vertex: UnionSet() for vertex in graph}

# sort the edges in the graph in ascending order in a list called edges:
edges = []
seen = set() # to avoid duplicate edges

for u in graph:
    for v, weight in graph[u].items():
        if (v, u) not in seen: # ensure we don't add both (A, B) and (B, A)
            edges.append((weight, sets[u], sets[v], u, v))
            seen.add((u, v))

# Sort edges by weight in ascending order
edges.sort(key=lambda edge: edge[0])

# Apply Kruskal's algorithm
MST = [] # minimum spanning tree

for weight, u, v, u_name, v_name in edges:
    if u.find() != v.find(): # only if they are in different sets
        MST.append((u_name, v_name, weight)) # Store the edge (A, B, eight)
        u.union(v) # merge sets

# Print Minimum Spanning Tree
for edge in MST:
    print(f"{edge[0]} - {edge[1]} -> {edge[2]}")