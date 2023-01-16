from numpy import Infinity

box = {'pieces': 21, 'red': 'R', 'yellow' : 'Y', 'title' : "Connect Four"}

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print("")

def transposed(board):
    result = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    return result

    
def check_winner(planche):
    trans = transposed(planche)
    winner = None
    for row in planche:
        counter = 0
        current_color = "( )"
        for spot in row:
            if spot != "( )" and current_color == "( )":
                current_color = spot
                counter = 1
            elif spot != "( )" and spot == current_color:
                counter += 1
            elif spot != "( )" and spot != current_color:
                current_color = spot
                counter = 1
            else:
                current_color = spot
                counter = 0
            if counter >= 4:
                winner = current_color

    if winner != None:
        return winner

    for row in trans:
        counter = 0
        current_color = "( )"
        for spot in row:
            if spot != "( )" and current_color == "( )":
                current_color = spot
                counter = 1
            elif spot != "( )" and spot == current_color:
                counter += 1
            elif spot != "( )" and spot != current_color:
                current_color = spot
                counter = 1
            else:
                current_color = spot
                counter = 0
            if counter >= 4:
                winner = current_color

    for i in range(0, len(planche), 1):
        for j in range(0, len(planche[0]), 1):
            pass

    return winner 

