"""
Tic Tac Toe Player
"""
import copy

import math

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
    count_x = 0
    count_o = 0

    if board == initial_state():
        return "X"
    
    for i in range(len(board)):
        for n in range(len(board[0])):
            if board[i][n] == "X":
                count_x += 1
            elif board[i][n] == "O":
                count_o += 1
    
    if count_x <= count_o:
        return "X"
    else:
        return "O" 


def actions(board):
    list = set()

    for i in range(len(board)):
        for n in range(len(board[0])):
            if board[i][n] == None:
                list.add((i,n))

    return list

def result(board, action):
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] != None:
        raise Exception
    elif new_board[action[0]][action[1]] == None:
        new_board[action[0]][action[1]] = player(new_board)

    return new_board


def winner(board):
    if board == initial_state():
        return None
        # Horizontal conditions
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return board[2][0]
        
        #Vertical conditions
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
        
        #Diagonal conditions
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    return None

def terminal(board):
    if winner(board) != None:
        return True

    for i in board:
        if EMPTY in i:
            return False
                
    return True

def utility(board):
    if winner(board) == "O":
        return -1
    elif winner(board) == "X":
        return 1
    else:
        return 0


def minimax(board):
    if board == terminal(board):
        return None

    if player(board) == "X":
        target = -math.inf
        target_act = None
        action_list = actions(board)

        for i in action_list:
            value = minvalue(result(board,i))

            if value > target:
                target = value
                target_act = i

        return target_act
    
    elif player(board) == "O":
        target = math.inf
        target_act = None

        action_list = actions(board)

        for i in action_list:
            value = maxvalue(result(board,i))

            if value < target:
                target = value
                target_act = i

        return target_act

def minvalue(board):
    if terminal(board):
        return utility(board)
    
    max = math.inf
    for action in actions(board):
        max = min(max, maxvalue(result(board, action)))
    
    return max

def maxvalue(board):
    if terminal(board):
        return utility(board)
    
    min = -math.inf
    for action in actions(board):
        min = max(min, minvalue(result(board, action)))
    
    return min
