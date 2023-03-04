import random
import re


class GameService:
    def __init__(self, repo):
        self._repo = repo



    def vin_sobolanii(self, x):
        if x == 1:
            y = random.randint(1, 10)
            self._repo.rats = int(self._repo.stocks * y / 100)
            self._repo.stocks = int(self._repo.stocks - self._repo.rats)

    def harvest_grain(self, user_input):
        """
        the function checks if the current population can harvest that many acres and then adjusts the stocks
        accordingly
        :param user_input:
        :return:
        """
        possible_harvest = self._repo.population * 10
        self._repo.stocks = self._repo.stocks - 2 * int(user_input)
        if int(user_input) - possible_harvest > 0:
            self._repo.stocks = self._repo.stocks + possible_harvest * (self._repo.harvest + 1)
        else:
            self._repo.stocks = self._repo.stocks + int(user_input) * self._repo.harvest

    def feed(self, user_input):
        """
        the function feeds the population accordingly to the user input and updates the starved counter and the new
        people counter from repo based on the user input
        :param user_input:
        :return:
        """
        ppl_fed = int(user_input) / 20
        self._repo.new = 0
        self._repo.starved = int(ppl_fed - self._repo.population)
        if abs(self._repo.starved) > self._repo.population / 2:
            return False
        if self._repo.starved >= 0:
            self._repo.starved = 0
            self._repo.new = random.randint(0, 10)
        self._repo.population = self._repo.population + self._repo.starved + self._repo.new
        self._repo.stocks = self._repo.stocks - int(user_input)
        return True

    def buy_land(self, user_input):
        """
        buys/sells land based on the user input and updates the stock and the area counters
        :param user_input:
        :return:
        """
        self._repo.area += int(user_input)
        self._repo.stocks = self._repo.stocks - self._repo.land_price * int(user_input)

    def set_harvest(self):
        value = random.randint(1, 6)
        self._repo.harvest = value

    def set_price(self):
        value = random.randint(15, 25)
        self._repo.land_price = value

    def __str__(self):
        message = ""
        message = message + "In year " + str(self._repo.turn) + ", " + str(abs(self._repo.starved)) + " people starved."
        message = message + "\n"
        message = message + str(self._repo.new) + " people came to the city."
        message = message + "\n"
        message = message + "City population is " + str(self._repo.population)
        message = message + "\n"
        message = message + "City owns " + str(self._repo.area) + " acres of land."
        message = message + "\n"
        message = message + "Harvest was " + str(self._repo.harvest) + " units per acre"
        message = message + "\n"
        message = message + "Rats ate " + str(self._repo.rats) + " units."
        message = message + "\n"
        message = message + "Land price is " + str(self._repo.land_price) + " units per acre."
        message = message + "\n"
        message = message + "\n"
        message = message + "Grain stocks are " + str(self._repo.stocks) + " units."
        return message


class Validator:
    def __init__(self, repo):
        self._repo = repo

    def validate_land(self, user_input):
        if re.match("[-+]?\d+$", user_input) is None:
            raise ValueError(">input has to be an integer")
        if int(user_input) * int(self._repo.land_price) > int(self._repo.stocks):
            raise ValueError(">you cant buy more land than you have grain for")
        if int(self._repo.area) + int(user_input) < 0:
            raise ValueError(">you cant sell more land than you have")

    def validate_grain(self, user_input):
        if str(user_input).isnumeric() is False:
            raise ValueError(">input has to be a positive integer")
        if int(user_input) > self._repo.stocks:
            raise ValueError(">you cannot feed people with grain you do not have")

    def validate_planting(self, user_input):
        if str(user_input).isnumeric() is False:
            raise ValueError(">input has to be a positive integer")
        if int(user_input) > self._repo.area:
            raise ValueError(">you cannot plant more acres than you have")
        if int(user_input) > self._repo.stocks:
            raise ValueError(">you cannot plant grain that you do not have")
