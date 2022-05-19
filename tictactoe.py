"""
Tic Tac Toe Player
"""

from ctypes import util
import math
import copy
from re import U

from numpy import maximum

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X 
    elif board != initial_state():
        xcount = 0
        ocount = 0 
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    xcount+=1
                if board[i][j] == "O":
                    ocount+=1
        if xcount > ocount:
            return O
        else:
            return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copyboard = copy.deepcopy(board)
    if action in actions(board):
        i = action[0]
        j = action[1]
        copyboard[i][j] = player(board)
    return copyboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # check rows 
        if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
            return X
        if board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
            return O
        # check columns
        if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            return X
        if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            return O

        # check diagonals
        if board[0][0] == board[1][1] == board[2][2] != EMPTY:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != EMPTY:
            return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if len(actions(board)) == 0 or winner(board) != None:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # this returns the best possible (i,j) pattern. which is then used in the results function.
    if terminal(board):
        return None

    if player(board) == X: # maximiaze the score. 
        pick = maximum(board)
        return pick

    else: # player == O minimiaze  the score 
        pick = minimum(board)
        return pick
    
def maximum(board):
    v = float('-inf')
    for action in actions(board):
        i = minvalue(result(board, action))
        if i > v:
            v = i
            pick = action  
    return pick

def minimum(board):      
    v = float('inf')
    for action in actions(board):
        i = minvalue(result(board, action))
        if i < v:
            v = i
            pick = action  
    return pick

def minvalue(board):

    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
    return v
    

def maxvalue(board):

    if terminal(board):
        return utility(board)

    v = float("-inf")
    for action in actions(board): 
        v = max(v, minvalue(result(board, action)))
    return v
    