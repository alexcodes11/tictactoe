"""
Tic Tac Toe Player
"""

import math
import copy

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
                else:
                    ocount+=1
                if xcount > ocount:
                    return O
                else:
                    return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = ()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions =  actions + ((i,j),)
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

   
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
