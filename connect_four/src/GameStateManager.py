from .states.MenuState import MenuState
from .states.PlayState import PlayState

class GameStateManager:

    clicked = False
    exit = False 

    def __init__(self, state, game, window):
        self.game = game
        self.window = window
        if state == "MENU":
            self.state = MenuState(game, window)
        elif state == "PLAY":
            self.state = PlayState(game, window)
        else:
            self.state = MenuState(game, window)
        
        self.state.set_gsm(self)
        
    
    def switch_state(self, state):
        if state == "MENU":
            self.state = MenuState(self.game, self.window)
        elif state == "PLAY":
            self.state = PlayState(self.game, self.window)
        else:
            self.state = MenuState(self.game, self.window)
        self.state.set_gsm(self)

    def update(self):
        self.state.update()
    
    def draw(self):
        self.state.draw()
    
