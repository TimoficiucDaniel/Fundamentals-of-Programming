class Repo:
    def __init__(self, board):
        self.__board = board

    @property
    def board(self):
        return self.__board

    def update(self, column, row, piece):
        self.__board.board[row][column] = piece


#idk = Board()
#repository = Repo(idk)
#repository.update(4,' ◯ ')
#repository.update(5,' ◍ ')
#print(repository.board())