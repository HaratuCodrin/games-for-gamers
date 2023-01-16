from src.table.GameSession import Session 



if __name__ == "__main__":

    options = [
        ["################## Connect Four ###################",
        "1. Start new game.",
        "2. Quit"],

        ["################## Connect Four ###################",
        "1. Pick a color.",
        "2. Go Back to Main Menu",
        "3. Quit."],

        ["################## Connect Four ###################",
        "1. Yellow",
        "2. Red",
        ],


        ["Board:"]
    ]
    state = 0
    game = None

    while True:
        for option in options[state]:
            print(option)
        
        if state < 3:
            choice = input("Your choice:")
            choice = choice.strip()
        else:
            print("Your Color: ", game.player_color)

        # main menu
        if state == 0:
            if choice == "1":
                state = 1
            elif choice == "2":
                print("Bye Bye!")
                exit(1)
        # choose to pick a color.
        elif state == 1:
            if choice == "1":
                state = 2
            elif choice == "2":
                state = 0
            elif choice == "3":
                print("Bye Bye!")
                exit(1)
        # picking a color.
        elif state == 2:
            if choice == "1":
                game = Session('yellow')
            elif choice == "2":
                game = Session('red')
            state = 3    
        # actual play state.
        elif state == 3:
            game.print_board()
            if game.yellow_pieces == 0 and game.red_pieces == 0:
                print("Game Over, conclusion: ", game.check_winner())
                state = 0
                game = None
            elif game.check_winner() != 'Tie':
                print("Game Over, conclusion: ", game.check_winner())
                state = 0
                game = None
            else:
                column = -1
                while column < 1 or column > 7:
                    print("Pick a column from 1 to 7,")
                    column = int(input(" to place a piece in:"))
                game.place_piece(game.player_color, column)
                game.print_board()
                if game.yellow_pieces == 0 and game.red_pieces == 0:
                    print("Game Over, conclusion: ", game.check_winner())
                    state = 0
                    game = None
                elif game.check_winner() != 'Tie':
                    print("Game Over, conclusion: ", game.check_winner())
                    state = 0
                    game = None
                game.random_ai_move()

            input("Press Anything to continue.")
            
        

            

        





