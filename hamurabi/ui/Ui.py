import random
import copy
from repo.Repository import Repository


class Ui:
    def __init__(self, game_service, validator, repo):
        self._game_service = game_service
        self._validator = validator
        self._repo = repo

    def start_program(self):
        self._game_service.set_harvest()
        self._game_service.set_price()
        x = random.randint(1, 5)
        self._game_service.vin_sobolanii(x)
        a = copy.deepcopy(self._repo.population)
        b = copy.deepcopy(self._repo.area)
        c = copy.deepcopy(self._repo.stocks)
        d = copy.deepcopy(self._repo.turn)
        e = copy.deepcopy(self._repo.starved)
        f = copy.deepcopy(self._repo.new)
        g = copy.deepcopy(self._repo.land_price)
        h = copy.deepcopy(self._repo.harvest)
        i = copy.deepcopy(self._repo.rats)
        second_repo = Repository(a, b, c, d, e, f, g, h, i)
        while self._repo.turn <= 5:
            try:
                self._repo = None
                self._repo = second_repo
                self.print()
                acres_buy_sell = input("Acres to buy/sell(+/-) ->")
                self._validator.validate_land(acres_buy_sell)
                self._game_service.buy_land(acres_buy_sell)
                units_to_feed = input("Units to feed the population ->")
                self._validator.validate_grain(units_to_feed)
                game_state = self._game_service.feed(units_to_feed)
                if game_state is False:
                    print("More than half of your population starved oh no! ")
                    break
                acres_to_plant = input("Acres to plant ->")
                self._validator.validate_planting(acres_to_plant)
                self._game_service.harvest_grain(acres_to_plant)
                self._game_service.set_harvest()
                self._game_service.set_price()
                x = random.randint(1, 5)
                self._game_service.vin_sobolanii(x)
                self._repo.turn += 1
                a = copy.deepcopy(self._repo.population)
                b = copy.deepcopy(self._repo.area)
                c = copy.deepcopy(self._repo.stocks)
                d = copy.deepcopy(self._repo.turn)
                e = copy.deepcopy(self._repo.starved)
                f = copy.deepcopy(self._repo.new)
                g = copy.deepcopy(self._repo.land_price)
                h = copy.deepcopy(self._repo.harvest)
                i = copy.deepcopy(self._repo.rats)
                second_repo = Repository(a, b, c, d, e, f, g, h, i)
            except ValueError as ve:
                print(str(ve))
        if self._repo.population > 100 and self._repo.area > 1000:
            print("lmao you won nice!")
        else:
            print("xd loser")

    def print(self):
        print(str(self._game_service))
