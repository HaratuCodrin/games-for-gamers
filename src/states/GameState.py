
class GameState:
    gsm = None
    def __init__(self, game, window):
        self.game = game
        self.window = window
        self.main_surface = self.game.Surface((self.window.get_width(), self.window.get_height()))

    def draw(self):
        self.window.blit(self.main_surface, (0, 0))

    def update(self):
        pass

    def set_gsm(self, gsm):
        self.gsm = gsm

    def input(self):
        self.mouse_x, self.mouse_y = self.game.mouse.get_pos()

        
        

    


        
        

        