from repo.Repository import Repository
from service.GameService import GameService
from service.GameService import Validator
from ui.Ui import Ui

repo = Repository(100, 1000, 3000, 1, 0, 0, 20, 3, 0)
game_service = GameService(repo)
validator = Validator(repo)
ui_part = Ui(game_service, validator, repo)

ui_part.start_program()
