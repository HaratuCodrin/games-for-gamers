from .GameState import GameState

class PlayState(GameState):

    planche = [
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""]
    ]



    def __init__(self, game, window, color = "RED"):
        super().__init__(game, window)
        self.player_color = color
        if color == "RED":
            self.ai_color = "YELLOW"
        else:
            self.ai_color = "RED"

    
    
