import random


class Bot:
    def __init__(self, game_service, repo):
        self.__game_service = game_service
        self.__repo = repo

    def make_a_play(self, turn):
        if turn == 2:
            random_play = random.randint(1, 7)
            self.__game_service.play_piece(random_play, ' ◍ ')
        else:
            i, j = self.check_player_about_to_win(' ◍ ')
            if i == -1 and j == -1:
                i, j = self.check_player_about_to_win(' ◯ ')
                if i == -1 and j == -1:
                    random_play = random.randint(1, 7)
                    self.__game_service.play_piece(random_play, ' ◍ ')
                else:
                    self.__game_service.play_piece(j + 1, ' ◍ ')
            else:
                self.__game_service.play_piece(j + 1, ' ◍ ')
                state = self.__game_service.check_board_state(' ◍ ')
                if state is True:
                    return "Computer wins!"
        return None

    def check_player_about_to_win(self, piece):
        for i in reversed(range(6)):
            for j in reversed(range(7)):
                if self.__repo.board.board[i][j] == piece:
                    win_counter = 0
                    for x in range(4):
                        if i - x >= 0:
                            if win_counter == 3 and self.__repo.board.board[i - x][j] == '\t':
                                    if i - x + 1 <= 5:
                                        if self.__repo.board.board[i - x + 1][j] != '\t':
                                            return i - x, j
                            if self.__repo.board.board[i - x][j] == piece:
                                win_counter += 1
                            else:
                                break
                    win_counter = 0
                    for x in range(4):
                        if i - x >= 0 and j - x >= 0:
                            if win_counter == 3 and self.__repo.board.board[i - x][j - x] == '\t':
                                if i - x + 1 <= 5:
                                    if self.__repo.board.board[i - x + 1][j - x] != '\t':
                                        return i-x , j-x
                            if self.__repo.board.board[i - x][j - x] == piece:
                                win_counter += 1
                            else:
                                break
                    win_counter = 0
                    for x in range(4):
                        if j - x >= 0:
                            if win_counter == 3 and self.__repo.board.board[i][j - x] == '\t':
                                if i + 1 <= 5:
                                    if self.__repo.board.board[i + 1][j - x] != '\t':
                                        return i, j - x
                                elif i == 5:
                                    return i, j - x
                            if self.__repo.board.board[i][j - x] == piece:
                                win_counter += 1
                            else:
                                break
                    win_counter = 0
                    for x in range(4):
                        if i + x <= 5 and j - x >= 0:
                            if win_counter == 3 and self.__repo.board.board[i + x][j - x] == '\t':
                                if i + x + 1 <= 5:
                                    if self.__repo.board.board[i + x + 1][j - x] != '\t':
                                        return i + x, j - x
                                    elif i+x == 5:
                                        return i + x, j - x
                            if self.__repo.board.board[i + x][j - x] == piece:
                                win_counter += 1
                            else:
                                break
                    win_counter = 0
                    for x in range(4):
                        if i + x <= 5 and j + x <= 6:
                            if win_counter == 3 and self.__repo.board.board[i + x][j + x] == '\t':
                                if i + x + 1 <= 5:
                                    if self.__repo.board.board[i + x + 1][j + x] != '\t':
                                        return i + x, j + x
                                elif i+x == 5:
                                    return i + x, j + x
                            if self.__repo.board.board[i + x][j + x] == piece:
                                win_counter += 1
                            else:
                                break
                    win_counter = 0
                    for x in range(4):
                        if j + x <= 6:
                            if win_counter == 3 and self.__repo.board.board[i][j + x] == '\t':
                                if i + 1 <= 5:
                                    if self.__repo.board.board[i + 1][j + x] != '\t':
                                        return i, j + x
                                elif i == 5:
                                    return i, j + x
                            if self.__repo.board.board[i][j + x] == piece:
                                win_counter += 1
                            else:
                                break
                    win_counter = 0
                    for x in range(4):
                        if i - x >= 0 and j + x <= 6:
                            if win_counter == 3 and self.__repo.board.board[i - x][j + x] == '\t':
                                if i - x + 1 <= 5:
                                    if self.__repo.board.board[i - x + 1][j + x] != '\t':
                                        return i - x, j + x
                            if self.__repo.board.board[i - x][j + x] == piece:
                                win_counter += 1
                            else:
                                break
        return -1, -1
