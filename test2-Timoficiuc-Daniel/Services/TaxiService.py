import random
from Domain.Taxi import Taxi
from Domain.Coordinates import Coordinate

class TaxiService:
    def __init__(self, taxi_repo):
        self.__taxi_repo = taxi_repo

    def generate_taxis(self, value):
        i = 1
        while int(value) >= int(i):
            location_x = random.randint(0, 100)
            location_y = random.randint(0, 100)
            location = Coordinate(location_x, location_y)
            generated_taxi = Taxi(i, 0, location)
            if len(self.__taxi_repo.object_list) > 0:
                aux = True
                for taxis in self.__taxi_repo.object_list:
                    if abs(generated_taxi.coordinates.x - taxis.coordinates.x) + \
                            abs(generated_taxi.coordinates.y - taxis.coordinates.y) > 5:
                        aux = False
                if aux == True:
                    self.__taxi_repo.add(generated_taxi)
                    i += 1
            else:
                self.__taxi_repo.add(generated_taxi)
                i += 1

    def show_taxis(self):
        return str(self.__taxi_repo)
