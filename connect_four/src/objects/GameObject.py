

class GameObject:
    dx = 0
    dy = 0
    def __init__(self, x, y, game, window):
        self.x = x
        self.y = y
        self.game = game
        self.window = window
        self.surface = self.game.Surface((10,10))

    # movement of the object     
    def update(self):
        pass

    # what is to be rendered by the object 
    def draw(self):
        self.window.blit(self.surface, (self.x, self.y))
        




