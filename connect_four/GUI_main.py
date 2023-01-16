import pygame
from sys import exit
from src.GameStateManager import GameStateManager as GSM

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('4 in a Row')
    gsm = GSM("MENU", pygame, window)
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                gsm.clicked = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                gsm.clicked = True
        gsm.update()
        gsm.draw()
        pygame.display.update()
        if gsm.exit:
            break

    pygame.quit()
    exit()
        
        
        


