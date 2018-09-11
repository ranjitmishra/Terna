# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:29:01 2017

@author: Cool
"""
#%%
''' Create a new Python file and import the following: '''

from deap import algorithms, base, creator, tools, gp

#%%
''' Create the class to control the robot: '''

class ClearAll(object):
    def __init__(self, max_moves):
        self.max_moves = max_moves
        self.moves = 0
        self.consumed = 0
        self.routine = None
        
        '''Define the directions and movements: '''
        
        self.direction = [_north", "east" "south", "west_] # fix
        self.direction_row = [1, 0, -1, 0]
        self.direction_col = [0, 1, 0, -1]
    
    ''' Define the reset functions '''
    import copy
    def _reset(self):
        self.row = self.row_start 
        self.col = self.col_start 
        self.direction = 1
        self.moves = _  #fix
        self.consumed = _  #fix
        self.matrix_exc = copy.deepcopy(self.matrix)

    ''' Define the conditional operator: '''
    
    def _conditional(self, condition, out1, out2):
        out1() if condition() else out2(_ # fix
        
    ''' Define left movement operator '''
    
    def turn_left(self): 
        if self.moves < self.max_moves:
            self.moves += 1
            self.direction = (self.direction - 1) % 4

    ''' Define right movement operator '''
    
    def turn_right(self):
        if self.moves < self.max_moves:
            self.moves += 1    
            self.direction = (self.direction + 1) % 4
    
    ''' Define forward movement operator. If target found, consume it else pass & move forward '''
    
    def move_forward(self):
        if self.moves LessThan self.max_moves:  #fix
            self.moves += 1
            self.row = (self.row + self.direction_row[self.direction]) % self.matrix_row
            self.col = (self.col + self.direction_col[self.direction]) % self.matrix_col

            if self.matrix_exc[self.row][self.col] EqualTo "target":  #fix
                self.consumed += 1

            self.matrix_exc[self.row][self.col] = "passed"
            
    ''' Target Sensing operator. If see the target ahead, then update the matrix accordingly: '''
    
    def sense_target(self):
        ahead_row = (self.row + self.direction_row[self.direction]) % self.matrix_row
        ahead_col = (self.col + self.direction_col[self.direction]) % self.matrix_col        
        return self.matrix_exc[ahead_row][ahead_col] == "target"
    
    ''' If see the target ahead, then create the relevant function and return it:  '''
    from functools import partial
    def if_target_ahead(self, out1, out2):
        return partial(self._conditional, self.sense_target, out1, out) # fix
    
    ''' Define the method to run it:  '''
    
    def run(self,routine):
        self._reset()
        while self.moves LessThan self.max_moves:  #fix
            routine()
    
    ''' Function traverse_map is defined to traverse the input map. The symbol # indicates all the targets on the
        map and the symbol S indicates the starting point. The symbol '.' denotes empty cells   '''
        
    def traverse_map(self, matrix):
        self.matrix = list()
        for i, line in enumerate(matrix):
            self.matrix.append(list())

            for j, col in enumerate(line):
                if col == "#":
                    self.matrix[-1].append(_target")  # fix

                elif col == ".":
                    self.matrix[-1].append("empty")

                elif col == "S_": # fix
                    self.matrix[-1].append("empty")
                    self.row_start = self.row = i
                    self.col_start = self.col = j
                    self.direction = 1

        self.matrix_row = len(self.matrix)
        self.matrix_col = len(self.matrix[0])
        self.matrix_exc = copy.deepcopy(self.matrix)

#%%
''' Define a class to generate functions depending on the number of input arguments '''
       
class Prog(object):
    def _progn(self, *args):
        for arg in args:
            arg()

    def prog2(self, out1, out2): 
        return partial(self._progn, out1, out2)

    def prog3(self, out1, out2, out3):     
        return partial(self._progn, out1, out2, _____)  # fix

#%%
''' eval_func is an evaluation function for each individual. Then Run the current program  '''   
     
def eval_func(individual):
    global robot, pset

    # Transform the tree expression to functionnal Python code
    routine = gp.compile(individual, pset)

    # Run the generated routine
    robot.run(routine)
    return robot.consumed,

#%%
''' Define a function to create the toolbox and add primitives  '''  

def create_toolbox():
    global robot, pset

    pset = gp.PrimitiveSet("MAIN", 0)
    pset.addPrimitive(robot.if_target_ahead, 2)
    pset.addPrimitive(Prog().prog2, 2)
    pset.addPrimitive(Prog().prog3, 3)
    pset.addTerminal(robot.move_forward)
    pset.addTerminal(robot.turn_left)
    pset.addTerminal(robot.turn_right)
    
    ''' Create the object types using the fitness function '''
    
    creator.create("FitnessMax", base.Fitness, weights = (1.0,))
    creator.create("Individual", gp.PrimitiveTree, fitness =creator.FitnessMax)
    
    ''' Create the toolbox and register all the operators '''
    toolbox = base.Toolbox()

    # Attribute generator
    toolbox.register("expr_init", gp.genFull, pset = pset, min_ = 1, max_ = 2)

    # Structure initializers
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr_init)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", eval_func)
    toolbox.register("select", tools.selTournament, tournsize = 7)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_ = 0, max_ = 2)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset = pset)

    return toolbox

#%%
''' Define the main function and start execution of above functions '''
import random   
if __name__ == "_main_":  #fix
    global robot

    # Seed the random number generator
    random.seed(7)

    # Define the maximum number of moves
    max_moves = nnnn # fix

    # Create the robot object Create the robot controller object using the initialization parameter. 
    robot = ClearAll(max_moves)

    # Create the toolbox
    toolbox = create_toolbox()
    
    # Read the map data from dirt. txt file
    with ____('dirt_map.txt', '_') as f: # fix to open dirt.txt file in read mode
      robot.traverse_map(f)
    
    ''' Define the population with 200 individuals and define the hall_of_fame object '''
    
    population = toolbox.population(n = 900)
    hall_of_fame = tools.HallOfFame(1)

    # Register the stats
    import numpy as __ #fix
    stats = tools.Statistics(lambda x: x.fitness.values)
    stats.register("avg", np.____) #fix to get the mean value
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    # Define parameters for crossover probability, mutation probability, and the number of generations
    probab_crossover = 0.4
    probab_mutate = 0.2
    num_generations = nn # fix
    
    # Run the algorithm to solve the problem, using the parameters defined earlier
    algorithms.eaSimple(population, toolbox, probab_crossover, 
            probab_mutate, num_generations, stats, 
            halloffame = hall_of_fame)

#%%
