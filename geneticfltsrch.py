# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 18:03:03 2018

@author: Cool
"""

#%%
import time
import random
#import math

#%%

people = [('Laxmi','BOS'),
          ('Deepa','DAL'),
          ('Raman','CAK'),
          ('Shiraj','MIA'),
          ('Dave','ORD'),
          ('Heena','OMA')]

#%%
# LaGuardia airport in New York. 
# flightsched.txtx - contains origin, destination, departure time, arrival time, and price for a set
# of flights in a comma-separated format:

destination='LGA'

flights={}
#
file = open(r"flightsched.txt")

'''
Load this data into a dictionary with the origin and destination (dest) as the keys
and a list of potential flight details as the values.
'''

for line in file:
    origin,dest,depart,arrive,price=line.strip( ).split(',')
    flights.setdefault((origin,dest),[])
    
    # Add details to the list of possible flights
    flights[(origin,dest)].append((depart,arrive,int(price)))

#%%
'''
Define a utility function, getminutes, which calculates how many minutes into the day a given time is.

This makes it easy to calculate flight times and waiting times.
'''
#%%

def getminutes(t):
    x = time.strptime(t,'%H:%M')
    return x[3]*60+x[4]

#%%
''' Lets create a routine that prints all the flights that people decide to take in a nice table. '''
def printschedule(r):
    
    for d in range(int(len(r)/2)):
        
        name = people[d][0]
        origin = people[d][1]
        out = flights[(origin,destination)] [r[d]]
        ret = flights[(destination,origin)] [r[d + 1]]
        
        print ('%10s%10s %5s-%5s $%3s %5s-%5s $%3s' %\
               (name,origin,\
                out[0],out[1],out[2],\
                ret[0],ret[1],ret[2]))
        
#%%
'''
This will print a line containing each person’s name and origin, as well as the departure
time, arrival time, and price for the outgoing and return flights.
'''

s = [1,4,3,2,7,3,6,3,2,4,5,3]

print("     A sample proposed schedule is: ")
printschedule(s)

#%%
'''
This function takes into account the total cost of the trip and the total time spent waiting
at airports for the various members of the family. It also adds a penalty of $50 if the
car is returned at a later time of the day than when it was rented.
'''
def schedulecost(sol):
    totalprice = 0
    latestarrival = 0
    totalwait = 0
    earliestdep = 24*60
               
    for d in range(int(len(sol)/2)):
        
        # Get the inbound and outbound flights
        origin = people[d][1]
        outbound = flights[(origin,destination)] [int(sol[d])]
        returnf = flights[(destination,origin)] [int(sol[d + 1])]
      
        # Total price is the price of all outbound and return flights
        totalprice += outbound[2]
        totalprice += returnf[2]
     
        # Track the latest arrival and earliest departure
        if latestarrival < getminutes(outbound[1]):
            latestarrival = getminutes(outbound[1])
            
        if earliestdep > getminutes(returnf[0]):
            earliestdep = getminutes(returnf[0])

     
 # Every person must wait at the airport until the latest person arrives.
 # They also must arrive at the same time and wait for their return flights.
     
    for d in range(int(len(sol)/2)):
        
        origin = people[d][1]
        outbound = flights[(origin,destination)] [int(sol[d])]
        returnf = flights[(destination,origin)] [int(sol[d + 1])]
        totalwait += latestarrival - getminutes(outbound[1])
        totalwait += getminutes(returnf[0]) - earliestdep
        
    # Does this solution require an extra day of car rental? That'll be $50!
    if latestarrival > earliestdep: totalprice += 50
    return totalprice + totalwait
    
    #%%
    
schedulecost(s)

#%%
''' The function takes several parametrs - 

popsize - The size of the population
mutprob - The probability that a new member of the population will be a mutation rather than a crossover
elite - The fraction of the population that are considered good solutions are allowed to pass into the next generation
maxiter - The number of generations to run
'''
#%%
def geneticoptimize(domain, costf, popsize = 50, step = 1,
                        mutprob = 0.2, elite = 0.2, maxiter = 100):
    
    # Mutation Operation
    def mutate(vec):
        i = random.randint(0, len(domain) - 1)
        if random.random() < 0.5 and vec[i] > domain[i][0]:
            return vec[0:i] + [vec[i] - step] + vec[i + 1:]
        elif vec[i] < domain[i][1]:
            return vec[0:i] + [vec[i] + step] + vec[i + 1:]
    
    # Crossover Operation
    def crossover(r1,r2):
        i = random.randint(1, len(domain) - 2)
        return r1[0:i] + r2[i:]
    
    # Build the initial population
    pop=[]
    for i in range(popsize):
        vec = [random.randint(domain[i] [0], domain[i] [1])
            for i in range(len(domain))]
        pop.append(vec)
    
    # How many winners from each generation?
    topelite = int(elite * popsize)
    
    # Main loop
    for i in range(maxiter):
        scores = [(costf(v),v) for v in pop]
        scores.sort( )
        ranked = [v for (s,v) in scores]
        
        # Start with the pure winners
        pop = ranked[0 : topelite]
        
        # Add mutated and bred forms of the winners
        while len(pop)<popsize:
            if random.random( ) < mutprob:
           
                # Mutation
                c = random.randint(0, topelite)
                pop.append(mutate(ranked[c]))
            else:
               
                # Crossover
                c1 = random.randint(0, topelite)
                c2 = random.randint(0, topelite)
                pop.append(crossover(ranked[c1], ranked[c2]))
            
            # Print current best score
        print (scores[0] [0])
    return scores[0] [1]
#%%
    
domain = [(0, 8)] * (len(people) * 2)

s = geneticoptimize(domain, schedulecost)

printschedule(s)

#%%

