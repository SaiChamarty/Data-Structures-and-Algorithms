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
