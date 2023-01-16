import copy
from numpy import Infinity

def available_moves(position):
    moves = []
    for i in range(0, len(position), 1):
        for j in range(0, len(position[0]), 1):
            if position[i][j] == "( )":
                moves.append([i, j])
    return moves

def print_board(board):
    for row in board:
        for column in row:
            print(column, end=" ")
        print("")

def static_eval(position):
    winner = check_winner(position)
    if winner == "(O)":
        return -1
    elif winner == "(X)":
        return 1
    else:
        return 0

def check_end(position):
    available = available_moves(position)
    if len(available) == 0 or check_winner(position) != 0:
        return True
    else:
        return False

def check_winner(position):
    # row check
    for i in range(0, len(position), 1):
        if equals(position[i][0], position[i][1], position[i][2]):
            return position[i][0]

    #column check
    for j in range(0, len(position), 1):
        if equals(position[0][j], position[1][j], position[2][j]):
            return position[0][j]
    
    # diagonal check
    if equals(position[0][0], position[1][1], position[2][2]) or equals(position[2][0], position[1][1], position[0][2]):
        return position[1][1]
        
    return 0

def equals(p1, p2, p3):
    if p1 == p2 and p2 == p3 and p1 != "( )":
        return True
    else:
        return False

def minimax(position, is_maximizing, depth):
    if depth == 0 or check_end(position):
        return static_eval(position)
    
    childMoves = available_moves(position)

    if is_maximizing:
        max_eval = -Infinity
        for move in childMoves:
            child = copy.deepcopy(position)
            child[move[0]][move[1]] = "(X)"
            eval = minimax(child, False, depth - 1)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        minEval = +Infinity
        for move in childMoves:
            child = copy.deepcopy(position)
            child[move[0]][move[1]] = "(O)"
            eval = minimax(child, True, depth - 1)
            minEval = min(minEval, eval)
        return minEval