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



#%%


