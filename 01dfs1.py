# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 22:47:55 2017

@author: Cool
"""

'''
Depth First Search (DFS), Breadth First Search (BFS) are search techniques that are commonly used on graphs to
 get to the solution. These are examples of uninformed search. They do not use any prior information
or rules to eliminate some paths. They check all the plausible paths and pick the optimal one.

Depth-First search which as the name hints at, explores possible vertices (from a supplied root) down each 
branch before backtracking. This property allows the algorithm to be implemented succinctly in both iterative 
and recursive forms.

Create an adjacency list which stores each node in a dictionary along with a set containing their
adjacent nodes. We use stack in the case of DFS because  Stack uses last-in-first-out ordering.
'''
#%%

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#%%

'''
Below is a listing of the actions performed upon each visit to a node - 

Mark the current vertex as being visited.
Explore each adjacent vertex that is not included in the visited set.

The implementation below uses the stack data-structure to build-up and return a set of vertices that 
are accessible within the subjects connected component. Using Python’s overloading of the subtraction
operator to remove items from a set, we are able to add only the unvisited adjacent vertices.

Graphs may contain cycles (which is the case here), so we may come to the same node again. To avoid 
processing a node more than once, we use a boolean visited array.

'''
#%%
# Connected Component

def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(graph[vertex] - set(visited))
            print(str(visited))
    return visited

dfs(graph, 'B')

 #%%

'''
Paths
We are able to tweak the previous implementations to return all possible paths between a start and goal vertex.
The implementation below uses the stack data-structure again to iteratively solve the problem, yielding each
 possible path when we locate the goal. Using a generator allows the user to only compute the desired amount of
 alternative paths.

'''
#%%%

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

list(dfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

#%%