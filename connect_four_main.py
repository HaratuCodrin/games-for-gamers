import copy
from random import *
from numpy import Infinity
import pygame
from connect_four import *
yellow_pieces = red_pieces = box['pieces']

planche = [
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""]
]

human = 'yellow'
ai = "red"

current_player = human

pygame.init()
screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption('4 in a Row')
clock = pygame.time.Clock()

# lanes = []
# for i in range(0, 7, 1):
#     lanes.append(pygame.Surface((100, 600)))
lane = pygame.Surface((100, 600))

board_surface = pygame.Surface((700, 600))
board_surface.fill('White')

board_width = board_surface.get_width()
board_height = board_surface.get_height()

# function for making a move


def place_piece(color, column):
    global yellow_pieces, red_pieces
    c = column - 1
    if color == 'yellow' and yellow_pieces == 0:
        return
    if color == 'red' and red_pieces == 0:
        return

    spots = planche[c]
    for i in range(len(spots)):
        k = len(spots) - i - 1
        if spots[k] == "( )":
            spots[k] = "(" + box[color] + ")"
            if color == 'yellow':
                yellow_pieces -= 1
            else:
                red_pieces -= 1
            break


def clear_planche():
    for i in range(0, len(planche), 1):
        for j in range(0, len(planche[0]), 1):
            planche[i][j] = "( )"


def update():
    global mouse_x, mouse_y
    mouse_x, mouse_y = pygame.mouse.get_pos()


def draw_piece(type, i, j):
    x = i * 100
    y = j * 100
    color = None

    if type == "(Y)":
        color = 'Yellow'
    elif type == "(R)":
        color = 'Red'
    else:
        return

    pygame.draw.circle(board_surface, color, (x + 50, y + 50), 40, 0)


def draw_planche():

    trans = planche
    screen.blit(board_surface, (0, 0))
    for i in range(1, len(planche), 1):
        x = i * board_width / 7
        pygame.draw.line(board_surface, 'Black', (x, 0), (x, board_height), 2)

    for i in range(1, len(planche[0]), 1):
        y = i * board_height / 6
        pygame.draw.line(board_surface, 'Black', (0, y), (board_width, y), 2)

    for i in range(0, len(trans), 1):
        for j in range(0, len(trans[0])):
            draw_piece(trans[i][j], i, j)


def draw():
    draw_planche()
    if check_winner(planche) == None:
        for i in range(0, len(planche), 1):
            x1 = i * board_width / 7
            x2 = (i+1) * board_width / 7
            if mouse_x >= x1 and mouse_x <= x2:
                screen.blit(lane, (i*100, 0))
                lane.set_alpha(100)
                if current_player == human:
                        lane.fill('Yellow')
                else:
                        lane.fill('Red')


if __name__ == "__main__":
    clear_planche()
    place_piece('red', 3)

    print_board(transposed(planche))
    print("Winner:", check_winner(planche))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(1)

            if event.type == pygame.MOUSEBUTTONUP and current_player == human and check_winner(planche) == None:
                place_piece(human, int(mouse_x / 100) + 1)
                current_player = ai
                break

            if event.type == pygame.MOUSEBUTTONUP and current_player == ai and check_winner(planche) == None:
                place_piece(ai, int(mouse_x / 100) + 1)
                current_player = human
                break

        # if current_player == ai and check_winner(planche) == None:
        #     place_piece(ai, randint(1, 7))
        #     current_player = human

        update()
        draw()
        pygame.display.update()
        clock.tick(60)
