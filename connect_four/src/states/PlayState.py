from .GameState import GameState
from src.table.GameSession import Session

class PlayState(GameState):

    def __init__(self, game, window, color = "red"):
        super().__init__(game, window)
        self.session = Session(color)
        self.lane = self.game.Surface((100,600))
        self.board_width = self.main_surface.get_width()
        self.board_height = self.main_surface.get_height() 
        self.player_turn = False    
        self.timer = 0   

    def draw_piece(self, type, i, j):
        x = i * 100
        y = j * 100
        color = None

        if type == "(Y)":
            color = 'Yellow'
        elif type == "(R)":
            color = 'Red'
        else:
            return

        self.game.draw.circle(self.main_surface, color, (x + 50, y + 50), 40, 0)

    def draw_planche(self):
        trans = self.session.planche
        for i in range(1, len(trans), 1):
            x = i * self.board_width / 7
            self.game.draw.line(self.main_surface, 'Black', (x, 0), (x, self.board_height), 2)

        for i in range(1, len(trans[0]), 1):
            y = i * self.board_height / 6
            self.game.draw.line(self.main_surface, 'Black', (0, y), (self.board_width, y), 2)

        for i in range(0, len(trans), 1):
            for j in range(0, len(trans[0])):
                self.draw_piece(trans[i][j], i, j)

    def draw(self):
        super().draw()
        self.input()
        self.main_surface.fill('White')
        self.draw_planche()
        planche = self.session.planche
        if self.session.check_winner() == 'Tie' and self.player_turn:
            for i in range(0, len(planche), 1):
                x1 = i * self.board_width / 7
                x2 = (i+1) * self.board_width / 7
                if self.mouse_x >= x1 and self.mouse_x <= x2:
                    self.window.blit(self.lane, (i*100, 0))
                    self.lane.set_alpha(100)
                    self.lane.fill(self.session.player_color)
    
    def update(self):
        self.input()

        if self.session.check_winner() == 'Tie' and self.session.yellow_pieces > 0 and self.session.red_pieces > 0:

            if not self.player_turn:
                self.timer += 1
                if self.timer >= 60:
                    self.timer = 0
                    self.player_turn = True
                    self.session.random_ai_move()

            if self.gsm.clicked and self.player_turn:
                self.session.place_piece(self.session.player_color, (int)(self.mouse_x/100) + 1)
                self.player_turn = False

        if self.gsm.main_menu:
            self.gsm.main_menu = False
            self.gsm.switch_state("MENU")


        
    
        
            


    
    
