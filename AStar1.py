# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 19:57:57 2017

@author: Cool
"""
#%%
'''
A* search gives the shortest path with lowest cost.

- Instead of blindly guessing where to go next, the A* algorithm picks the one that looks the most promising. At each
  node, we generate the list of all possibilities and then pick the one with the minimal cost required to reach the goal.

- At each node, we need to compute the cost. This cost is basically the sum of two costs – the first cost is the 
    cost of getting to the current node and the second cost is the cost of reaching the goal from the current node.
    We use this summation as our heuristic. The second cost is basically an estimate that's not usually
    perfect.  Organizations have their own techniques to calculate the cost. 

- It takes some time to find the best path to the solution. A* is very effective in finding the optimal paths 
    and is one of the most popular techniques out there. Let's use the A* algorithm to build a maze solver. 

'''
#%%
''' 
Use the below maze. The # symbols indicate obstacles. The symbol o represents the starting point and x
represents the goal. Our goal is to find the shortest path from the start to the end point. Let's
see how to do it in Python. 
    ##############################
    #         #              #   #
    # ####    ########       #   #
    #  o #    #              #   #
    #    ###     #####  ######   #
    #      #   ###   #           #
    #      #     #   #  #  #   ###
    #     #####    #    #  # x   #
    #              #       #     #
    ##############################

'''
#%%
#import the following packages: (simpleai is in local folder, where code is stored)

import math
import numpy as np
from simpleai.search import SearchProblem, astar

#%%
'''
Create a class that contains the methods needed to solve the problem
'''
#%%

class MazeSolver(SearchProblem):
    # Initialize the class 
    def __init__(self, board):
        self.board = board
        self.goal = (0, 0)
        # Extract the initial and final positions:
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x].lower() == "o":
                    self.initial = (x, y)
                elif self.board[y][x].lower() == "x":
                    self.goal = (x, y)
        # Use built-in function called “super,” which returns a proxy object to delegate method calls to class
        # MazeSolver
        super(MazeSolver, self).__init__(initial_state=self.initial)

    ''' Define the method that takes actions
     to arrive at the solution. At each position, we need to check the cost of going to the
     neighboring cells and then append all the possible actions. If the neighboring cell is blocked,
     then that action is not considered:
    '''

    def actions(self, state):
        actions = []
        
        for action in COSTS.keys():
            newx, newy = self.result(state, action)
            if self.board[newy][newx] != "#":
                actions.append(action)
                
        print('unique actions :', np.unique(actions))
        return actions
       
    # Update the state based on the action. Depending on the current state and the input action, update
    # the x and y coordinates:
    
    def result(self, state, action):
        x, y = state
        
        if action.count("up"):
            y -= 1
        if action.count("down"):
            y += 1
        if action.count("left"):
            x -= 1
        if action.count("right"):
            x += 1
        
        new_state = (x, y)

        return new_state

    # Check if we have reached the goal
    def is_goal(self, state):
        return state == self.goal

    # Compute the cost of taking an action. We need to define the cost function. This is the cost of moving to
    # a neighboring cell, and it's different for vertical/horizontal and diagonal moves.
    
    def cost(self, state, action, state2):
        return COSTS[action]

    # Heuristic that we use to arrive at the solution. In this case, we will use the Euclidean distance:
    
    def heuristic(self, state):
        x, y = state
        gx, gy = self.goal

        return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)

#%%
        
'''
Define the main function and also define the map we discussed earlier:

'''
        
if __name__ == "__main__":
    # Define the map
    MAP = """
    ##############################
    #         #              #   #
    # ####    ########       #   #
    #  o #    #              #   #
    #    ###     #####  ######   #
    #      #   ###   #           #
    #      #     #   #  #  #   ###
    #     #####    #    #  # x   #
    #              #       #     #
    ##############################
    """

    # Convert map to a list
    print(MAP)
    MAP = [list(x) for x in MAP.split("\n") if x]
#%%
    # Define cost of moving around the map. The diagonal move is more expensive than
    # horizontal or vertical moves:
    
    cost_regular = 1.0
    cost_diagonal = 1.7

    # Create the cost dictionary
    COSTS = {
        "up": cost_regular,
        "down": cost_regular,
        "left": cost_regular,
        "right": cost_regular,
        "up left": cost_diagonal,
        "up right": cost_diagonal,
        "down left": cost_diagonal,
        "down right": cost_diagonal,
    }

#%%
    # Create maze solver object
    problem = MazeSolver(MAP)

    # Run the solver on the map and extract the result:
    result = astar(problem, graph_search=True)

    # Extract the path from the result:
    path = [x[1] for x in result.path()]

    # Print the result
    print()
    print(" The Shortest Path With Lowest Cost is - ")
    print()
    for y in range(len(MAP)):
        for x in range(len(MAP[y])):
            if (x, y) == problem.initial:
                print('o', end='')
            elif (x, y) == problem.goal:
                print('x', end='')
            elif (x, y) in path:
                print('·', end='')
            else:
                print(MAP[y][x], end='')

        print()

#%%


