from Service.GameException import GameError


class GameService:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def __str__(self):
        message = ""
        for lists in self.__repo.board.board:
            message = message + "|"
            for elements in lists:
                message = message + elements + ','
            message = message + "|"
            message = message + "\n"
        return message

    def play_piece(self, column, piece):
        self.__validator.validate_play(column)
        column = int(column) - 1
        row = -1
        for i in reversed(range(6)):
            if self.__repo.board.board[i][column] == '\t':
                row = i
                break
        if row == -1:
            raise GameError(["invalid location"])
        self.__repo.update(column, row, piece)

    def check_board_state(self, piece):
        for i in range(6):
            for j in range(7):
                if self.__repo.board.board[i][j] == piece:
                    win = self.check_win(i, j, piece)
                    if win is True:
                        return True
        return False

    def check_win(self, i, j, piece):
        win_counter = 0
        for x in range(4):
            if i - x >= 0:
                if self.__repo.board.board[i - x][j] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for x in range(4):
            if i - x >= 0 and j - x >= 0:
                if self.__repo.board.board[i - x][j - x] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for x in range(4):
            if j - x >= 0:
                if self.__repo.board.board[i][j - x] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for x in range(4):
            if i + x <= 5 and j - x >= 0:
                if self.__repo.board.board[i + x][j - x] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for x in range(4):
            if i + x <= 5:
                if self.__repo.board.board[i + x][j] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for x in range(4):
            if i + x <= 5 and j + x <= 6:
                if self.__repo.board.board[i + x][j + x] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for x in range(4):
            if j + x <= 6:
                if self.__repo.board.board[i][j + x] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for x in range(4):
            if i - x >= 0 and j + x <= 6:
                if self.__repo.board.board[i - x][j + x] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        return False


class Validator:
    def __init__(self):
        pass

    def validate_play(self, column):
        if str(column).isnumeric() is False:
            raise GameError(["invalid input for a column"])
        if int(column) < 1 or int(column) > 7:
            raise GameError(["invalid location"])
