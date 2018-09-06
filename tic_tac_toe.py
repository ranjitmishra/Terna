# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 13:59:57 2018

@author: Cool
"""

#%%
"""
The Negamax algorithm is a variant of Minimax that's frequently used in real world
implementations.

A two-player game is usually a zero-sum game, which means that one
player's loss is equal to another player's gain and vice versa.

Negamax uses this property extensively to come up with a strategy to increases its chances of
winning the game. In terms of the game, the value of a given position to the first player is
the negation of the value to the second player. Each player looks for a move that will maximize
the damage to the opponent. The value resulting from the move should be such that the opponent
gets the least value.
This works both ways seamlessly, which means that a single method can be
used to value the positions. This is where it has an advantage over Minimax in terms of
simplicity. Minimax requires that the first player select the move with the maximum value,
whereas the second player must select a move with the minimum value.
"""
#%%
# Intall easyAI by pip - pip3 install easyAI. Create a new Python file and import the following packages-

from easyAI import TwoPlayersGame, AI_Player, Human_Player, Negamax
#from easyAI.Player import 

#%%
''' Define a class that contains all the methods to play the game. Start by defining the players
and who starts the game: '''

class GameController(TwoPlayersGame):
    def __init__(self, players):
        # Define the players
        self.players = players

        # Define who starts the game
        self.nplayer = 1 

        # Define the board. lets use a 3×3 board numbered from one to nine row-wise
        self.board = [0] * 9
    
    # Define a method to compute all the possible moves
    def possible_moves(self):
        return [a + 1 for a, b in enumerate(self.board) if b == 0]
    
    # Define a method to update the board after making a move. Make a move
    def make_move(self, move):
        self.board[int(move) - 1] = self.nplayer

    # Does the opponent have three in a line? Define a method to see if somebody has lost 
    # the game. We will be checking if somebody has three in a row
    def loss_condition(self):
        return any( [all([(self.board[i - 1] == self.nopponent)
                    for i in line])
                    for line in [[1,2,3],[4,5,6],[7,8,9], # horiz.
                                   [1,4,7],[2,5,8],[3,6,9], # vertical
                                   [1,5,9],[3,5,7]]]) # diagonal
        
    # Check if the game is over using the loss_condition method
    def is_over(self):
        return (self.possible_moves() == []) or self.loss_condition()
        
    # Show current position
    def show(self):
        print('\n'+'\n'.join([' '.join([['.', 'O', 'X'][self.board[3*j + i]]
                for i in range(3)]) for j in range(3)]))
                 
    # Compute the score using the loss_condition method
    def scoring(self):
        return -100 if self.loss_condition() else 0

#%%
# Define the main function and start by defining the algorithm.
# We can specify the number of steps in advance that the algorithm should think.
# In this case, let's choose 5:
        
if __name__ == "__main__":
    
    algorithm = Negamax(5)

    # Start the game
    GameController([Human_Player(), AI_Player(algorithm)]).play()

#%%