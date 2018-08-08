# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:12:56 2017

@author: Cool
"""
#%%
'''
BFS visits all the nodes of a graph (connected component) following a breadthward motion. In other words, BFS
 starts from a node, then it checks all the nodes at distance one from the starting node, then it checks all
 the nodes at distance two and so on. In order to remember the nodes to be visited, BFS uses a queue. The 
 algorithm can keep track of the vertices it has already checked to avoid revisiting them, in case a graph had
 one or more cycles.
'''
#%%
# A sample graph implemented as a dictionary
graph = {'A': ['B', 'E', 'C'],
         'B': ['A','E', 'D'],
         'C': ['A', 'F', 'G'],
         'D': ['B', 'E'],
         'E': ['A', 'B','D'],
         'F': ['C'], 
         'G': ['C']}
print(graph)
#%%
'''
In particular, BFS follows the following steps:

Check the starting node and add its neighbours to the queue.
Mark the starting node as explored.
Get the first node from the queue / remove it from the queue
Check if node has already been visited.
If not, go through the neighbours of the node.
Add the neighbour nodes to the queue.
Mark the node as explored.
Loop through steps 3 to 7 until the queue is empty.

To implement the BFS queue a FIFO (First In, First Out) is used. In FIFO queues, the oldest (first) entry is
processed first. 
'''
#%%

# visits all the nodes of a graph (connected component) using BFS
# Once the while loop is exited, the function returns all of the visited nodes
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
 
    # keep looping until there are nodes still to be checked
    n = 0
    while queue:
        n = n + 1
        print('loop - ', n)
        # pop shallowest node (first node) from queue
        print('queue:', queue)
        node = queue.pop(0)
        print('node :', node)
        
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
            print('neigh ;', neighbours)
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored

bfs_connected_component(graph,'A')# returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']

#%% 

'''
That’s it! We have a functioning BFS implementation that traverses a graph. Now on to a more challenging task:
    finding the shortest path between two nodes.
For this task, the function we implement should be able to accept as argument a graph, a starting node 
(e.g., ‘G’) and a node goal (e.g., ‘D’). The nice thing about BFS is that it always returns the shortest path, even if 
 there is more than one path that links two vertices.

There are a couple of main differences between the implementations of BFS for traversing a graph and for
 finding the shortest path. First, in case of the shortest path application, we need for the queue to keep
 track of possible paths (implemented as list of nodes) instead of nodes. Second, when the algorithm checks
 for a neighbour node, it needs to check whether the neighbour node corresponds to the goal node. If that’s the
 case, we have a solution and there’s no need to keep exploring the graph.

'''
#%%

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [start]
 
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
    n = 0 
    # keeps looping until all possible paths have been checked
    while queue:
        n = n + 1
        print('loop :', n)
        print('queue :', queue)
        # pop the first path from the queue
        path = queue.pop(0)
        print('path :', path)
        # get the last node from the path
        node = path[-1]
        print('node :', node)
        if node not in explored:
            print('explored :', explored)
            neighbours = graph[node]
            print('neighbours :', neighbours)
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                print('neighbour :', neighbour)
                new_path = list(path)
                print('new_path :', new_path)
                new_path.append(neighbour)
                print('new_path1 :', new_path)
                queue.append(new_path)
                print('new_path2 :', new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    print('neighbour1 :', neighbour)
                    print('new_path3 :', new_path)
                    return new_path
                
                # mark node as explored
            explored.append(node)
            print('explored1 :', explored)
 
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist."
 
bfs_shortest_path(graph, 'G', 'T')  # returns ['G', 'C', 'A', 'B', 'D']

#%%

'''
The good and the bad of BFS
There’s a great news about BFS: it’s complete. That’s because this algorithm is always able to find a solution
 to a problem, if there is one. For example, if a path exists that connects two nodes in a graph, BFS will 
 always be capable of identifying it – given the search space is finite.

Completeness is a nice-to-have feature for an algorithm, but in case of BFS it comes to a high cost. The 
execution time of BFS is fairly slow, because the time complexity of the algorithm is exponential. What’s 
worse is the memory requirements. That’s because BFS has to keep track of all of the nodes it explores. In the
case of problems which translate into huge graphs, the high memory requirements make the use of BFS unfeasible.

'''

