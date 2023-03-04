from Domain.Coordinates import Coordinate
import random

class RideService:
    def __init__(self, taxi_repo):
        self.__taxi_repo = taxi_repo

    def add_ride(self, ride_start_point, ride_end_point):
        max_distance = 100
        max_taxi_id = 0
        for taxis in self.__taxi_repo.object_list:
            distance = abs(ride_start_point.x - taxis.coordinates.x) + abs(ride_start_point.y - taxis.coordinates.y)
            if distance < max_distance:
                max_distance = distance
                max_taxi_id = taxis.id
            for taxis in self.__taxi_repo.object_list:
                if taxis.id == max_taxi_id:
                    taxis.fare = abs(ride_start_point.x - ride_end_point.x) + abs(ride_start_point.y - ride_end_point.y)
                    taxis.coordinates = ride_end_point

    def simulate_rides(self,value):
        for i in range(value):
            max_distance = 100
            ride_start_point = Coordinate(random.randint(0,100),random.randint(0,100))
            ride_end_point = Coordinate(random.randint(0,100),random.randint(0,100))
            for taxis in self.__taxi_repo.object_list:
                distance = abs(ride_start_point.x - taxis.coordinates.x) + abs(ride_start_point.y - taxis.coordinates.y)
                if distance < max_distance:
                    max_distance = distance
                    max_taxi_id = taxis.id
            for taxis in self.__taxi_repo.object_list:
                if taxis.id == max_taxi_id:
                    taxis.fare = abs(ride_start_point.x - ride_end_point.x) + abs(ride_start_point.y - ride_end_point.y)
                    taxis.coordinates = ride_end_point
                    print("taxi id is "+str(max_taxi_id)+" start location is " +str(ride_start_point)+" end location is "
                          +str(ride_end_point))




