

class Session:

    box = {'pieces': 21, 'red': 'R', 'yellow' : 'Y'}

    planche = [
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""]
    ]

    
    def __init__(self, player_color):
        self.player = self.box[player_color]
        self.yellow_pieces = self.red_pieces = self.box['pieces']
        
    def clear_planche(self):
        for i in range(0, len(self.planche), 1):
            for j in range(0, len(self.planche[0]), 1):
                self.planche[i][j] = "( )"

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


    def print_board(board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j], end=" ")
            print("")

    def transposed(board):
        result = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
        return result

