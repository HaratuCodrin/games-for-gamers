from random import choice, randint
from math import sin
from .GameObject import GameObject


class FloatingPiece(GameObject):

    A = 5
    w = 0.05
    
    def __init__(self, x, y, game, window):
        super().__init__(x, y, game, window)
        self.dx = randint(1,2)
        self.width = 50
        self.height = 50
        self.color = choice(['Yellow','Red'])
        self.surface = self.game.Surface((self.width, self.height))
        self.surface.set_colorkey((0,0,0))

    def update(self): 
        self.x += self.dx
        self.y += self.A*sin(self.w * self.x)

    def draw(self):
        super().draw()
        self.game.draw.circle(
            self.surface, self.color, 
            (self.width/2, self.height/2), 
            self.width/2, 0
            )
        