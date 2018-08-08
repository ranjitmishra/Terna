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
    # Innitialize visited list and stack 
    visited, stack = [], [start]
    print('visited :', visited)
    print('stack :', stack)
    n = 0
    # Keep looping till stack is empty
    while stack:
        n = n + 1
        print("Loop - ", n)
        print('stack1 :', stack)
        # Get the value from stack 
        vertex = stack.pop()
        print('stack2 :', stack)
        print('vertex :', vertex)
        # Check if the node is processed or not.
        if vertex not in visited:
            print('visited1 :', visited)
            # Add unvisited node to the visisted list now
            visited.append(vertex)
            print('visited2 :', visited)
            # Remove the visted/processed node from the stack
            stack.extend(graph[vertex] - set(visited))
            print('stack3 :', stack)
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
    # Initialize the stack with start value
    stack = [(start, [start])]
    print('stack :', stack)
    l = 0
    while stack:
        l = l + 1
        print("Loop - ", l)
        # Disect stack value as vertex and path
        (vertex, path) = stack.pop()
        print('vertex :', vertex)
        print('path :', path)
        # Loop until there is vertex to be checked. No need to look for next for the identified path
        for next in graph[vertex] - set(path):
            print('Next :', next)
            print("Graph Vertex - Path :", (graph[vertex] - set(path)))
            # If next value is same as the goal value, get path 
            if next == goal:
                # Use generator fucntion yield to not to loose local values in next loop of function execution
                yield path + [next]
                print("Path + Next :", (path + [next] ))
                print('stack1 :', stack)
            else:
                stack.append((next, path + [next]))
                print('stack2 :', stack)

list(dfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

#%%
