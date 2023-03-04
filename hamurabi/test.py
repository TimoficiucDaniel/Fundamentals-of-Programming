import unittest
from service.GameService import GameService
from repo.Repository import Repository


class TestGameService(unittest.TestCase):
    def setUp(self):
        self._repo = Repository(100, 1000, 3000, 1, 0, 0, 20, 3, 0)
        self._serv = GameService(self._repo)

    def test_harvest_grain(self):
        self._repo.population = int(100)
        self._repo.area = int(1000)
        self._repo.stocks = int(1000)
        self._repo.turn = int(1)
        self._repo.starved = int(0)
        self._repo.new = int(0)
        self._repo.land_price = int(20)
        self._repo.harvest = int(3)
        self._repo.rats = int(0)
        self._serv.harvest_grain(1000)
        self.assertEqual(2000,self._repo.stocks)
        self._repo.population = int(100)
        self._repo.area = int(2000)
        self._repo.stocks = int(2000)
        self._repo.turn = int(1)
        self._repo.starved = int(0)
        self._repo.new = int(0)
        self._repo.land_price = int(20)
        self._repo.harvest = int(3)
        self._repo.rats = int(0)
        self._serv.harvest_grain(2000)
        self.assertEqual(2000, self._repo.stocks)

    def test_feed(self):
        self._repo.population = int(100)
        self._repo.area = int(1000)
        self._repo.stocks = int(3000)
        self._repo.turn = int(1)
        self._repo.starved = int(0)
        self._repo.new = int(0)
        self._repo.land_price = int(20)
        self._repo.harvest = int(3)
        self._repo.rats = int(0)
        ceva = self._serv.feed(1600)
        self.assertEqual(True,ceva)
        self._repo.population = int(100)
        self._repo.area = int(1000)
        self._repo.stocks = int(3000)
        self._repo.turn = int(1)
        self._repo.starved = int(0)
        self._repo.new = int(0)
        self._repo.land_price = int(20)
        self._repo.harvest = int(3)
        self._repo.rats = int(0)
        ceva = self._serv.feed(2000)
        self.assertEqual(True, ceva)

    def test_buy_land(self):
        self._repo.population = int(100)
        self._repo.area = int(1000)
        self._repo.stocks = int(3000)
        self._repo.turn = int(1)
        self._repo.starved = int(0)
        self._repo.new = int(0)
        self._repo.land_price = int(20)
        self._repo.harvest = int(3)
        self._repo.rats = int(0)
        self._serv.buy_land(10)
        self.assertEqual(1010,self._repo.area)

    def tearDown(self):
        self._repo = None
        self._serv = None