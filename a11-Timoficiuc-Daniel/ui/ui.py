from Domain.Board import Board
from Repo.Repository import Repo
from Service.GameService import GameService
from Service.GameException import GameError
from Service.GameService import Validator
from Service.BOTService import Bot
board = Board()
repo = Repo(board)
validator = Validator()
serv = GameService(repo,validator)
bota = Bot(serv,repo)

class Start:
    def __init__(self,serv,bota):
        self.__game_service = serv
        self.__turn = 1
        self.__bot = bota

    def start_program(self):
        while True:
            try:
                #if self.__turn == 42:
                    if self.__turn % 2 == 1:
                        print(self.__game_service)
                        user_input = input("Where to play a piece? >")
                        self.__game_service.play_piece(user_input,' ◯ ')
                        state = self.__game_service.check_board_state(' ◯ ')
                        if state is True:
                            print(str(self.__game_service))
                            print("you win!")
                            return
                        self.__turn += 1
                    else:
                        cwin =self.__bot.make_a_play(self.__turn)
                        if cwin is not None:
                            print(str(self.__game_service))
                            print(cwin)
                            return
                        self.__turn +=1
                #else:
                 #   print("tie")
                   # return
            except GameError as ge:
                print(str(ge))

start = Start(serv,bota)
start.start_program()