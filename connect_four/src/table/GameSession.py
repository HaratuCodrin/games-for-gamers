
from random import randint, choice
from copy import deepcopy

class Session:

    box = {'pieces': 21, 'red': 'R', 'yellow' : 'Y'}

    ended = False

    planche = [
        ["( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )"]
    ]

    
    def __init__(self, player_color):
        self.clear_planche()
        self.player = self.box[player_color]
        self.player_color = player_color
        if self.player_color == 'yellow':
            self.ai_color = 'red'
        else:
            self.ai_color = 'yellow'
        self.yellow_pieces = self.red_pieces = self.box['pieces']
        
    def clear_planche(self):
        for i in range(0, len(self.planche), 1):
            for j in range(0, len(self.planche[0]), 1):
                self.planche[i][j] = "( )"

    def available_moves(self):
        moves = []
        for i in range(0, len(self.planche), 1):
            if self.planche[i][0] != '( )':
                moves.append(i)
        return moves

    def place_piece_in(self, y, r, color, column, planche):
        c = column - 1
        if color == 'yellow' and y == 0:
            return
        if color == 'red' and r == 0:
            return

        spots = planche[c]
        for i in range(len(spots)):
            k = len(spots) - i - 1
            if spots[k] == "( )":
                spots[k] = "(" + self.box[color] + ")"
                   

    def place_piece(self, color, column):
        c = column - 1
        if color == 'yellow' and self.yellow_pieces == 0:
            return
        if color == 'red' and self.red_pieces == 0:
            return

        spots = self.planche[c]
        for i in range(len(spots)):
            k = len(spots) - i - 1
            if spots[k] == "( )":
                spots[k] = "(" + self.box[color] + ")"
                if color == 'yellow':
                    self.yellow_pieces -= 1
                else:
                    self.red_pieces -= 1
                break

    def random_ai_move(self):
        column = randint(1, 7)
        self.place_piece(self.ai_color, column)
    
    def ai_move(self):
        board = self.transposed()
        moves = range(1,7,1)
        found = False
        for move in moves:
            checked_position = deepcopy(board)
            c = move - 1
            spots = checked_position[c]
            for i in range(len(spots)):
                k = len(spots) - i - 1
                if spots[k] == "( )":
                    spots[k] = "(" + self.box[self.player_color] + ")"
            if self.get_winner(checked_position) == "(" + self.box[self.player_color] + ")":
                self.place_piece(self.ai_color, move)
                found = True
                break
        
        if not found:
            self.random_ai_move()


    def get_winner(self, board):
        maxx = len(board[0]) - 1
        maxy = len(board) - 1
        winner = None
        directions = [
            [1,0],
            [1,-1],
            [1,1],
            [0,1]
        ]
        for d in directions:
            dx = d[0]
            dy = d[1]
            
            for x in range(0, maxx):
                for y in range(0, maxy):
                    lastx = x + 3 * dx
                    lasty = y + 3 * dy
                    if 0 <= lastx and lastx < maxx and 0 <= lasty and lasty < maxy:
                        spot = board[x][y]
                        if spot != "( )" and spot == board[x+dx][y+dy] and spot == board[x+2*dx][y+2*dy] and spot == board[lastx][lasty]:
                            winner = spot
        
        if winner == None:
            return 'Tie'
        else: return winner

    def check_winner(self):
        board = self.transposed()
        maxx = len(board[0]) - 1
        maxy = len(board) - 1
        winner = None
        directions = [
            [1,0],
            [1,-1],
            [1,1],
            [0,1]
        ]
        for d in directions:
            dx = d[0]
            dy = d[1]
            
            for x in range(0, maxx):
                for y in range(0, maxy):
                    lastx = x + 3 * dx
                    lasty = y + 3 * dy
                    if 0 <= lastx and lastx < maxx and 0 <= lasty and lasty < maxy:
                        spot = board[x][y]
                        if spot != "( )" and spot == board[x+dx][y+dy] and spot == board[x+2*dx][y+2*dy] and spot == board[lastx][lasty]:
                            winner = spot
        
        if winner == None:
            return 'Tie'
        else: return winner
    
    def print_board(self):
        board = self.transposed()
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j], end=" ")
            print("")

    def transposed(self):
        board = self.planche
        result = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
        return result

