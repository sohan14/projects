

class TicTacToe:
    def __init__(self):
        self.board={
            '1':' ',
            '2':' ',
            '3':' ',
            '4':' ',
            '5':' ',
            '6':' ',
            '7':' ',
            '8':' ',
            '9':' '
        }
    def create_board(self):
        print(f'   {self.board["7"]}   |  {self.board["8"]}    |  {self.board["9"]}   ')
        print('-----------------------')
        print(f'   {self.board["4"]}   |  {self.board["5"]}    |  {self.board["6"]}   ')
        print('-----------------------')
        print(f'   {self.board["1"]}   |  {self.board["2"]}    |  {self.board["3"]}   ')
    def update_board_x(self,x):
        x=x
        if self.board[x]==" ":
            self.board[x]='X'
            self.create_board()
            return False
        else:
            print('The position taken , try another position.')
            return True
    def update_board_y(self,y):
        y = y
        if self.board[y] == " ":
            self.board[y] = 'O'
            self.create_board()
            return False
        else:
            print('The position taken , try another position.')
            return True

    def check_win(self,X):

        if self.board["1"]==self.board["2"]==self.board["3"]==X:
            print(f'Player {X} won.')
            return False

        elif self.board["4"]==self.board["5"]==self.board["6"]==X:
            print(f'Player {X} won.')
            return False

        elif self.board["7"]==self.board["8"]==self.board["9"]==X:
            print(f'Player {X} won.')
            return False

        elif self.board["1"]==self.board["4"]==self.board["7"]==X:
            print(f'Player {X} won.')
            return False

        elif self.board["2"]==self.board["5"]==self.board["8"]==X:
            print(f'Player {X} won.')
            return False

        elif self.board["3"]==self.board["6"]==self.board["9"]==X:
            print(f'Player {X} won.')
            return False

        elif self.board["1"]==self.board["5"]==self.board["9"]==X:
            print(f'Player {X} won.')
            return False

        elif self.board["7"]==self.board["5"]==self.board["3"]==X:
            print(f'Player {X} won.')
            return False

        else:
            a=None
            for values in self.board.values():
                if values==" ":
                    a=True
                    break
                else:
                    a=False
            if a==False:
                print('Its a draw.')
            return a




