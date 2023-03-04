from Repository.Repository import Repository
from Domain.Taxi import Taxi
from Domain.Coordinates import Coordinate
from Services.RideService import RideService
from Services.TaxiService import TaxiService

taxi_repo = Repository()
taxi_services = TaxiService(taxi_repo)
ride_services = RideService(taxi_repo)


class start:
    def __init__(self, taxi_services, ride_services):
        self.__taxi_services = taxi_services
        self.__ride_services = ride_services

    @staticmethod
    def show_menu():
        print("1.Add ride")
        print("2.Simulate rides")
        print("3.Exit")

    def start_program(self):
        user_input = input("how many taxis? ")
        self.__taxi_services.generate_taxis(user_input)
        print(self.__taxi_services.show_taxis())
        while True:
            self.show_menu()
            option = input("which option?")
            option.strip(" ")
            if option == '1':
                start_x = input("start x = ")
                start_y = input("start y = ")
                end_x = input("end x = ")
                end_y = input("end y = ")
                start = Coordinate(start_x, start_y)
                end = Coordinate(end_x, end_y)
                self.__ride_services.add_ride(start, end)
                print(self.__taxi_services.show_taxis())
            elif option == '2':
                number_of_simulations = int(input("number of simulations ?"))
                self.__ride_services.simulate_rides(number_of_simulations)
                print(self.__taxi_services.show_taxis())
            elif option == '3':
                return


inceput = start(taxi_services, ride_services)
inceput.start_program()
