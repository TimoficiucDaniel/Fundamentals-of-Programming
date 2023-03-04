import copy


class Repository:
    def __init__(self, population, area, stocks, turn, starved, new, land_price, harvest, rats):
        self._population = population
        self._area = area
        self._stocks = stocks
        self._turn = turn
        self._starved = starved
        self._new = new
        self._land_price = land_price
        self._harvest = harvest
        self._rats = rats

    def __deepcopy__(self,memo):
        return Repository(copy.deepcopy(self._population,memo),
                          copy.deepcopy(self._area,memo),
                          copy.deepcopy(self._stocks,memo),
                          copy.deepcopy(self._turn,memo),
                          copy.deepcopy(self._starved,memo),
                          copy.deepcopy(self._new,memo),
                          copy.deepcopy(self._land_price,memo),
                          copy.deepcopy(self._harvest,memo),
                          copy.deepcopy(self._rats,memo))

    @property
    def rats(self):
        return self._rats

    @property
    def land_price(self):
        return self._land_price

    @property
    def harvest(self):
        return self._harvest

    @property
    def population(self):
        return self._population

    @property
    def area(self):
        return self._area

    @property
    def stocks(self):
        return self._stocks

    @property
    def new(self):
        return self._new

    @property
    def starved(self):
        return self._starved

    @property
    def turn(self):
        return self._turn

    @population.setter
    def population(self, value):
        self._population = value

    @area.setter
    def area(self, value):
        self._area = value

    @stocks.setter
    def stocks(self, value):
        self._stocks = value

    @starved.setter
    def starved(self, value):
        self._starved = value

    @new.setter
    def new(self, value):
        self._new = value

    @turn.setter
    def turn(self, value):
        self._turn = value

    @harvest.setter
    def harvest(self, value):
        self._harvest = value

    @land_price.setter
    def land_price(self, value):
        self._land_price = value

    @rats.setter
    def rats(self, value):
        self._rats = value
