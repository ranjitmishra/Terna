# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 11:13:31 2017

@author: Cool
"""

'''
Imeplementing MiniMax algorithm in a very simple way

Minimax (sometimes MinMax) is a decision rule used in decision theory, game theory, statistics and philosophy for
minimizing the possible loss for a worst case (maximum loss) scenario. When dealing with gains, it is referred to 
as "maximin"—to maximize the minimum gain.

It is an recursive algorithm used in two players games such as Tic Tac Toe, Chess etc to find the optimal moves.

How Does MinMax Algorithm Works in Tic Tac Toe?
Let’s say while playing Tic Tac Toe, we look at the board state and try to predict the future i.e
 we try to place a move that is best for us and worst for the opponent. The minmax algorithm works
 in the same manner. There are 255,168 different states in a game of Tic Tac Toe. 131,184 for first
 player, 77,904 for second player and 46,080 for a draw. Since a computer got more computational power,
 instead of only predicting the best move for the current state of board, it simulates the game for
 all possibles moves and plays till end forming a tree and backtracks to the current state knowing
 which move is best for it and worst for opponent

'''
#%%
import random

#%%
""" Create a class and Initialize with empty board"""

class TicTacToe:

    def __init__(self):
        
        self.board = [" ", " ", " ", 
                      " ", " ", " ", 
                      " ", " ", " "]
    
    """Format and print board"""
    def show(self):
        
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))

    ''' Return whoever wins '''
    def whoWon(self):
        if self.checkWin() == "X":
            return "You"
        elif self.checkWin() == "O":
            return "I"
        elif self.gameOver() == True:
            return "Nobody"

    """Return empty spaces on the board"""
    def availableMoves(self):
        
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    """Get all moves made by a given player"""
    def getMoves(self, player):
        
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == player:
                moves.append(i)
        return moves

    """Make a move on the board"""
    def makeMove(self, position, player):
        self.board[position] = player

    """Return the player that wins the game"""
    def checkWin(self):
        
        combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6])

        for player in ("X", "O"):
            positions = self.getMoves(player)
            for combo in combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player

    """Return True if X wins, O wins, or draw, else return False"""
    def gameOver(self):
        
        if self.checkWin() != None:
            return True
        for i in self.board:
            if i == " ":
                return False
        return True

    """
        Recursively analyze every possible game state and choose the best move location.
        node - the board
        depth - how far down the tree to look
        player - what player to analyze best move for (currently setup up ONLY for "O")
    """
    def minimax(self, node, depth, player):
        
        if depth == 0 or node.gameOver():
            if node.checkWin() == "X":
                return 0
            elif node.checkWin() == "O":
                return 100
            else:
                return 50

        if player == "O":
            bestValue = 0
            for move in node.availableMoves():
                node.makeMove(move, player)
                moveValue = self.minimax(node, depth - 1, changePlayer(player))
                node.makeMove(move, " ")
                bestValue = max(bestValue, moveValue)
                print(bestValue, moveValue)
            return bestValue
        
        if player == "X":
            bestValue = 100
            for move in node.availableMoves():
                node.makeMove(move, player)
                moveValue = self.minimax(node, depth - 1, changePlayer(player))
                node.makeMove(move, " ")
                bestValue = min(bestValue, moveValue)
            return bestValue

#%%
'''
change palyer to get other player play the game

'''
#%%
"""Returns the opposite player given any player"""        

def changePlayer(player):
    
    if player == "X":
        return "O"
    else:
        return "X"

#%%
"""
    Controllor function to initialize minimax and keep track of optimal move choices
    board - what board to calculate best move for
    depth - how far down the tree to go
    player - who to calculate best move for (Works ONLY for "O" right now)
"""        

def make_best_move(board, depth, player):
   
    neutralValue = 50
    choices = []
    for move in board.availableMoves():
        board.makeMove(move, player)
        moveValue = board.minimax(board, depth - 1, changePlayer(player))
        board.makeMove(move, " ")

        if moveValue > neutralValue:
            choices = [move]
            break
        elif moveValue == neutralValue:
            choices.append(move)
    
    if len(choices) > 0:
        return random.choice(choices)
    else:
        return random.choice(board.availableMoves())
    
#%%
'''
Lets play now

'''
#%%
#Actual game
if __name__ == '__main__':
    game = TicTacToe()
    game.show()

    while game.gameOver() == False:
        person_move = int(input("You are X: Choose number from 1-9: "))
        game.makeMove(person_move - 1, "X")
        game.show()

        if game.gameOver() == True:
            break
 
        ai_move = make_best_move(game, 2, "O")
        game.makeMove(ai_move, "O")
        game.show()

    print("Game Over. " + game.whoWon() + " Win")
    
#%%
