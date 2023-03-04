from repo.Repo import Repository
from domain.Question import Question
from service.GameService import Gameservice
from repo.Repo import Validator
from ui.ui import Ui

repo = Repository("myquiz.txt")
repo.load_file()
validator = Validator()
game_service = Gameservice(repo, validator)
ui = Ui(game_service, repo)

ui.start_program()
