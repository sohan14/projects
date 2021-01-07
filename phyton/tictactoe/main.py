from tictactoe import TicTacToe

game = TicTacToe()
game.create_board()
x = True
y = True
game_on = True
while game_on:
    while x:
        try:
            x = game.update_board_x(input('Player X, enter your position in board: '))
        except KeyError:
            print("Please enter number between 1-9 .")
        else:
            y = True
    game_on = game.check_win('X')
    if game_on:
        while y:
            try:
                y = game.update_board_y(input('Player O, enter your position in board: '))
            except KeyError:
                print("Please enter number between 1-9 .")
                y = True
            else:
                x = True
        game_on = game.check_win('O')
