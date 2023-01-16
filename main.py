import pygame
from sys import exit
from tic_tac_toe import *

board = [
    ["(X)", "", ""],
    ["", "(O)", "(O)"],
    ["", "(X)", ""]
]

AI = "(X)"
HUMAN = "(O)"

current_player = "(X)"
depth = 9

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()
board_surface = pygame.Surface((600, 600))
board_surface.fill('White')

board_width = board_surface.get_width()
board_height = board_surface.get_height()


def human_move(x, y):
    global current_player
    global winner
    i = y / (board_height / 3)
    j = x / (board_height / 3)
    i = int(i)
    j = int(j)

    if board[i][j] == "( )":
        make_move(i, j, HUMAN)
        winner = check_winner(board)
        if check_end(board):
            if winner == 0:
                winner = "Nobody"
            print(winner + " won!")
        else:
            current_player = AI


def drawX(surface, x, y, size):
    s = size / 4
    pygame.draw.line(surface, 'Black', (x + s, y + s),
                     (x + size - s, y + size - s), 4)
    pygame.draw.line(surface, 'Black', (x + s, y + size - s),
                     (x + size - s, y + s), 4)


def drawO(surface, x, y, size):
    s = size / 4
    pygame.draw.ellipse(surface, 'Black', (x + s, y + s, 2*s, 2*s), 4)


def drawBoard(surface):
    screen.blit(board_surface, (0, 0))
    pygame.draw.line(board_surface, 'Black', (board_width/3, 0),
                     (board_width/3, board_height), 5)
    pygame.draw.line(board_surface, 'Black', (2*board_width /
                     3, 0), (2*board_width/3, board_height), 5)
    pygame.draw.line(board_surface, 'Black', (0, board_height/3),
                     (board_width, board_height/3), 5)
    pygame.draw.line(board_surface, 'Black', (0, 2*board_height/3),
                     (board_width, 2*board_height/3), 5)


def update():
    global mouse_x, mouse_y
    mouse_x, mouse_y = pygame.mouse.get_pos()


def draw():
    # drawing the board
    drawBoard(board_surface)
    for i in range(0, len(board), 1):
        for j in range(0, len(board), 1):
            if board[i][j] == "(X)":
                drawX(board_surface, (j * board_width) / 3,
                      (i * board_height) / 3, board_width / 3)
            if board[i][j] == "(O)":
                drawO(board_surface, (j * board_width) / 3,
                      (i * board_height) / 3, board_width / 3)


def best_move(is_maximizing):
    global board, depth
    bestMove = None
    idealValue = None
    symToWrite = None
    moveSet = []

    if is_maximizing:
        symToWrite = "(X)"
        idealValue = -Infinity
    else:
        symToWrite = "(O)"
        idealValue = +Infinity

    for move in available_moves(board):
        newMove = copy.deepcopy(board)
        newMove[move[0]][move[1]] = symToWrite
        moveSet.append(newMove)

    for pos in moveSet:
        if is_maximizing:
            # eval = minimax(pos, False, len(available_moves(pos)))
            eval = minimax(pos, False, depth)
            if eval > idealValue:
                idealValue = eval
                bestMove = copy.deepcopy(pos)
        else:
            # eval = minimax(pos, True, len(available_moves(pos)))
            eval = minimax(pos, True, depth)
            if eval < idealValue:
                idealValue = eval
                bestMove = copy.deepcopy(pos)
    board = bestMove


def make_move(x, y, value):
    board[x][y] = value


def clear_board():
    for i in range(0, len(board), 1):
        for j in range(0, len(board[0]), 1):
            board[i][j] = "( )"


if __name__ == "__main__":
    clear_board()
    global winner
    while True:

        if current_player == AI and not check_end(board):
            # best line of code AI to move 
            best_move(AI == "(X)")
            winner = check_winner(board)
            if check_end(board):
                if winner == 0:
                    winner = "Nobody"
                print(winner + " won!")
            else:
                current_player = HUMAN

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and check_end(board):
                if event.key == pygame.K_ESCAPE: # reset game when ended 
                    clear_board()
                    board_surface.fill('White')
                    current_player = "(X)"

            if event.type == pygame.MOUSEBUTTONUP and current_player == HUMAN:
                human_move(mouse_x, mouse_y)

        # update everything
        update()
        # draw elements
        draw()
        # print(mouse_x, mouse_y)
        pygame.display.update()
        clock.tick(60)
