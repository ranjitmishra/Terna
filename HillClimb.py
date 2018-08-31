# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:47:13 2017

@author: Cool
"""
#%%

"""
Planning a trip for a group of people from different locations, all arriving at the same place is 
always a challenge, and it makes for an interesting optimization problem.

The friends are from all over the USA and wish to meet up in New York.

They will all arrive on the same day and leave on the same day, and they would like
to share transportation to and from the airport.

There are dozens of flights per day to New York from any of the members’ locations, all leaving at
different times. The flights also vary in price and in duration.

The challenge now is to decide which flight each person in the group should take. Of
course, keeping total price down is a goal, but there are many other possible factors
that the optimal solution will take into account and try to minimize, such as total
waiting time at the airport or total flight time. These other factors will be discussed
in more detail shortly.

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
'''
The optimization functions you’ll see later are generic enough to work on many different types of 
problems, so it’s important to choose a simple representation that’s not specific to the group travel 
problem. A very common representation is a list of numbers. In this case, each number can represent
which flight a person chooses to take, where 0 is the first flight of the day, 1 is the second,
and so on. Since each person needs an outbound flight and a return flight, the length of this list is twice
the number of people. 

For example, the list: [1,4,3,2,7,3,6,3,2,4,5,3] Represents a solution in which Laxmi 
takes the second flight of the day from Boston to New York, and the fifth flight back to Boston on the day
she returns. Deepa takes the fourth flight from Dallas to New York, and the third flight back.
'''
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
Even disregarding price, this schedule has some problems. In particular, since the
family members are traveling to and from the airport together, everyone has to arrive
at the airport quite early for return flight, even though some of them don’t leave
until nearly 4 p.m. To determine the best combination, the program needs a way of
weighing the various properties of different schedules and deciding which is the
best.

'''
#%%
'''
The cost function is the key to solving any problem using optimization, and it’s usually
the most difficult thing to determine. The goal of any optimization algorithm is
to find a set of inputs — flights, in this case — that minimizes the cost function, so the
cost function has to return a value that represents how bad a solution is. There is no
particular scale for badness; the only requirement is that the function returns larger
values for worse solutions.

Often it is difficult to determine what makes a solution good or bad across many variables.
Consider a few of the things that can be measured in the group travel example:
Price - The total price of all the plane tickets, or possibly a weighted average that takes
financial situations into account.

Travel time - The total time that everyone has to spend on a plane.

Waiting time - Time spent at the airport waiting for the other members of the party to arrive.

Departure time - Flights that leave too early in the morning may impose an additional cost by
requiring travelers to miss out on sleep.

Car rental period - If the party rents a car, they must return it earlier in the day than when they
rented it, or be forced to pay for a whole extra day.

'''
#%%
'''
This function takes into account the total cost of the trip and the total time spent waiting
at airports for the various members of the family. It also adds a penalty of $50 if the
car is returned at a later time of the day than when it was rented.
'''

def schedulecost(sol):
    totalprice = 0
    latestarrival = 0
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
    totalwait = 0
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

'''
Now that the cost function has been created, it should be clear that the goal is to
minimize cost by choosing the correct set of numbers. In theory, you could try every
possible combination, but in this example there are 16 flights, all with 9 possibilities,
giving a total of 9**16 (around 300 billion) combinations. Testing every combination
would guarantee you’d get the best answer, but it would take a very long time on
most computers.

'''

#%%

'''
The function takes a couple of parameters. Domain is a list of 2-tuples that specify the
minimum and maximum values for each variable. The length of the solution is the
same as the length of this list. In the current example, there are nine outbound flights
and nine inbound flights for every person, so the domain in the list is (0,8) repeated
twice for each person.

Hill climbing starts with a random solution and looks at the set of neighboring solutions for those that
are better (have a lower cost function). This is analogous to going down a hill.

We can apply this hill climbing approach to the task of finding the best travel
schedule for a group of friends. Start with a random schedule and find all the neighboring
schedules. In this case, that means finding all the schedules that have one person
on a slightly earlier or slightly later flight.

The cost is calculated for each of the neighboring schedules, and the one with the lowest cost becomes the new 
solution. This process is repeated until none of the neighboring schedules improves the cost.

'''
#%%
def hillclimb(domain,costf):
    # Create a random solution
    sol = [random.randint(domain[i][0],domain[i][1])
        for i in range(len(domain))]
    # Main loop
    while 1:
        # Create list of neighboring solutions
        
        neighbors = []
        for j in range(len(domain)):
            # One away in each direction
            
            if sol[j] > domain[j][0]:
                neighbors.append(sol[0:j] + [sol[j] +1] + sol[j + 1:])
            if sol[j] < domain[j][1]:
                neighbors.append(sol[0:j] + [sol[j] - 1] + sol[j + 1:])
        # See what the best solution amongst the neighbors is
        
        current = costf(sol)
        best = current
        for j in range(len(neighbors)):
            cost = costf(neighbors[j])
            if cost < best:
                best = cost
                sol = neighbors[j]

        # If there's no improvement, then we've reached the top
        if best == current:
            break
    return sol
#%%
  
domain = [(0,8)]*(len(people)*2)
    
s = hillclimb(domain, schedulecost)

print("Optimal Cost is: ", schedulecost(s))
print("")
print("The proposed schedule is:  ")
printschedule(s)

#%%


