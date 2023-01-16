from .GameState import GameState
from random import randint
from src.objects.FloatingPiece import FloatingPiece

class MenuState(GameState):

    pieces = []
    timer = 0
    frequency = 50
    options = ["Play Game", "Change Color: ", "Quit Game"]

    player_color = "RED"

    title1 = "CONNECT FOUR"
    title2 = "by Inès GRUJIC"


    def __init__(self, game, window):
        super().__init__(game, window)
        self.font_big = self.game.font.SysFont(None, 70)
        self.font_small = self.game.font.SysFont(None, 50)
        

    def draw(self):
        super().draw()
        self.main_surface.fill((21, 88, 67))
        for piece in self.pieces:
            piece.draw()

        titre_image_1 = self.font_big.render(self.title1, True, (0, 0, 0))
        titre_image_2 = self.font_small.render(self.title2, True, (0, 0, 0))
        self.window.blit(titre_image_1, (200, 220))
        self.window.blit(titre_image_2, (300, 280))

        for i in range(0, len(self.options)):
            option_x = 200
            option_y = 350 + 40 * i
            option = self.font_small.render(self.options[i], True, (211,211,211))
            if self.mouse_x > option_x and self.mouse_x < option_x + option.get_width():
                if self.mouse_y > option_y and self.mouse_y < option_y + option.get_height():
                    rect = option.get_rect()
                    self.game.draw.rect(option, (211,211,211), rect, 1)
            self.window.blit(option, (option_x, option_y))

    def update(self):
        self.timer += 1
        self.input()
        for i in range(0, len(self.options)):
            option_x = 200
            option_y = 350 + 40 * i
            option = self.font_small.render(self.options[i], True, (211,211,211))
            if self.mouse_x > option_x and self.mouse_x < option_x + option.get_width():
                if self.mouse_y > option_y and self.mouse_y < option_y + option.get_height():
                    if self.gsm.clicked:
                        if self.options[i] == "Play Game":
                            self.gsm.switch_state("PLAY")
                        elif self.options[i] == "Quit Game":
                            self.gsm.exit = True

        for piece in self.pieces:
            piece.update()
            if piece.x > self.window.get_width():
                self.pieces.remove(piece)
        if self.timer >= self.frequency:
            self.timer = 0
            print(len(self.pieces))
            piece = FloatingPiece(-20, 
                            randint(0, 400),
                            self.game, self.main_surface)
            self.pieces.append(piece)