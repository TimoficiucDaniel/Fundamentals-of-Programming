from domain.Client import ClientValidator
from domain.Movie import MovieValidator
from domain.Rental import RentalValidator
from domain.ValidatorException import ValidatorError
from repository.RepoException import RepoError
from repository.Repository import Repository
from services.ClientService import ClientService
from services.MovieService import MovieService
from services.RentalException import RentalError
from services.RentalService import RentalService
from services.UndoService import UndoRedo

import datetime

client_repo = Repository()
movie_repo = Repository()
rental_repo = Repository()
validator_client = ClientValidator()
validator_movie = MovieValidator()
validator_rental = RentalValidator()

ClientServices = ClientService(client_repo, rental_repo, validator_client)
MovieServices = MovieService(movie_repo, rental_repo, validator_movie)
RentalServices = RentalService(client_repo, movie_repo, rental_repo, validator_rental)
UndoServices = UndoRedo([], [], ClientServices, MovieServices, RentalServices)



class Start:
    def __init__(self, ClientServices, MovieServices, RentalServices, UndoServices):
        self._ClientServices = ClientServices
        self._MovieServices = MovieServices
        self._RentalServices = RentalServices
        self._client_id = 11111
        self._movie_id = 111111
        self._rental_id = 111
        self.__UndoServices = UndoServices

    def initiate_settings(self):
        pass

    def initialize_client_repo(self):
        self._ClientServices.create(self._client_id, "Andrei")
        self._client_id += 1
        self._ClientServices.create(self._client_id, "Mihai")
        self._client_id += 1
        self._ClientServices.create(self._client_id, "Viorel")
        self._client_id += 1
        self._ClientServices.create(self._client_id, "Andreea")
        self._client_id += 1
        self._ClientServices.create(self._client_id, "Alexa")
        self._client_id += 1

    def initialize_movie_repo(self):
        self._MovieServices.add(self._movie_id, "The Lord of the Rings", "cool movie", "Fantasy")
        self._movie_id += 1
        self._MovieServices.add(self._movie_id, "Interstellar", "another cool movie", "Mystery")
        self._movie_id += 1
        self._MovieServices.add(self._movie_id, "Emma", "random movie", "Romance")
        self._movie_id += 1
        self._MovieServices.add(self._movie_id, "Iron Man", "marvel movie", "Action")
        self._movie_id += 1
        self._MovieServices.add(self._movie_id, "Avengers", "another marvel movie", "Action")
        self._movie_id += 1

    def initialize_rental_repo(self):
        self._RentalServices.create_rental(self._rental_id, "111111", "11112", datetime.datetime(2021, 10, 7),
                                           datetime.datetime(2021, 10, 7) + datetime.timedelta(days=14), None)
        self._rental_id += 1
        self._RentalServices.create_rental(self._rental_id, "111113", "11111", datetime.datetime(2021, 11, 10),
                                           datetime.datetime(2021, 11, 10) + datetime.timedelta(days=14), None)
        self._rental_id += 1
        self._RentalServices.create_rental(self._rental_id, "111114", "11113", datetime.datetime(2021, 12, 1),
                                           datetime.datetime(2021, 12, 1) + datetime.timedelta(days=14), None)
        self._rental_id += 1
        self._RentalServices.create_rental(self._rental_id, "111115", "11114", datetime.datetime(2021, 11, 29),
                                           datetime.datetime(2021, 11, 29) + datetime.timedelta(days=14), None)
        self._rental_id += 1

    @staticmethod
    def show_general_menu():
        print("1.Add client")
        print("2.Delete client")
        print("3.Update client")
        print("4.List clients")
        print("5.Add movie")
        print("6.Delete movie")
        print("7.Update movie")
        print("8.List movies")
        print("9.Rent movie")
        print("10.Return movie")
        print("11.Search client/movie")
        print("12.List rentals")
        print("13.Statistics")
        print("14.Undo")
        print("15.Exit")

    @staticmethod
    def print_search_menu():
        print("1.Search client by name")
        print("2.Search client by id")
        print("3.Search movie by title")
        print("4.Search movie by id")
        print("5.Search movie by description")
        print("6.Search movie by genre")

    def search(self):
        self.print_search_menu()
        option = (input("Input: "))
        user_input = (input("Input to search by: "))
        if option == '1':
            list_to_print = self._ClientServices.search_by_name(user_input)
        elif option == '2':
            list_to_print = self._ClientServices.search_by_id(user_input)
        elif option == '3':
            list_to_print = self._MovieServices.search_by_title(user_input)
        elif option == '4':
            list_to_print = self._MovieServices.search_by_id(user_input)
        elif option == '5':
            list_to_print = self._MovieServices.search_by_description(user_input)
        elif option == '6':
            list_to_print = self._MovieServices.search_by_genre(user_input)
        else:
            return None
        if not list_to_print:
            raise ValueError(">no clients/movies found")
        return list_to_print

    @staticmethod
    def statistics_menu():
        print("1.Most rented movies.")
        print("2.Most active clients.")
        print("3.Late rentals.")

    def statistics(self):
        self.statistics_menu()
        option = (input("Input: "))
        if option == '1':
            result = self._RentalServices.most_rented_movies()
        elif option == '2':
            result = self._RentalServices.most_active_client()
        elif option == '3':
            result = self._RentalServices.late_rentals()
        else:
            return None
        return result

    def start_program(self):
        self.initialize_client_repo()
        self.initialize_movie_repo()
        self.initialize_rental_repo()
        while True:
            self.show_general_menu()
            option = (input("Input: "))
            option = option.strip(" ")
            try:
                if option == '1':
                    name = (input("Insert name: "))
                    block = self._ClientServices.create(self._client_id, name)
                    self._client_id += 1
                    self.__UndoServices.add_to_undo_history(block)
                elif option == '2':
                    client_id_to_delete = (input("Id of the client to be deleted: "))
                    undo_block = self._ClientServices.delete(client_id_to_delete)
                    self.__UndoServices.add_to_undo_history(undo_block)
                elif option == '3':
                    client_id_to_update = (input("Id of the client to be updated: "))
                    updated_name = (input("Updated name: "))
                    block = self._ClientServices.update(client_id_to_update, updated_name)
                    self.__UndoServices.add_to_undo_history(block)
                elif option == '4':
                    print(str(self._ClientServices.list()))
                elif option == '5':
                    title = (input("Title: "))
                    description = (input("Description: "))
                    genre = (input("Genre: "))
                    action = self._MovieServices.add(self._movie_id, title, description, genre)
                    self._movie_id += 1
                    self.__UndoServices.add_to_undo_history(action)
                elif option == '6':
                    movie_id_to_delete = (input("Id of the movie to be deleted: "))
                    block = self._MovieServices.delete(movie_id_to_delete)
                    self.__UndoServices.add_to_undo_history(block)
                elif option == '7':
                    movie_id_to_update = (input("Id of the movie to be updated: "))
                    updated_title = (input("Updated title: "))
                    updated_description = (input("Updated description: "))
                    updated_genre = (input("Updated genre:"))
                    block = self._MovieServices.update(movie_id_to_update, updated_title, updated_description,
                                                       updated_genre)
                    self.__UndoServices.add_to_undo_history(block)
                elif option == '8':
                    print(str(self._MovieServices.list()))
                elif option == '9':
                    rental_client_id = (input("Client id: "))
                    rental_movie_id = (input("Movie id: "))
                    year = int((input("Year: ")))
                    day = int((input("Day of the month (integer): ")))
                    month = int((input("Month of the year (integer): ")))
                    rented_date = datetime.datetime(year, month, day)
                    due_date = datetime.date.today() + datetime.timedelta(days=14)
                    returned_date = None
                    block = self._RentalServices.create_rental(self._rental_id, rental_movie_id,
                                                               rental_client_id, rented_date, due_date, returned_date)
                    self._rental_id += 1
                    self.__UndoServices.add_to_undo_history(block)
                elif option == '10':
                    rental_id_to_return = (input("Id of the rental to be returned: "))
                    returned_date = datetime.date.today()
                    self._RentalServices.rental_returned(rental_id_to_return, returned_date)
                elif option == '11':
                    result = self.search()
                    if result is None:
                        print("Incorrect input")
                    for elements in result:
                        print(str(elements))
                elif option == '12':
                    print(str(self._RentalServices.list()))
                elif option == '13':
                    result = self.statistics()
                    if result is None:
                        print("Incorrect input")
                    for elements in result:
                        print(str(elements))
                elif option == '14':
                    self.__UndoServices.undo()
                elif option == '15':
                    return
                else:
                    print("Incorrect input.")
            except ValueError as ve:
                print(str(ve))
            except ValidatorError as vae:
                print(str(vae))
            except RepoError as re:
                print(str(re))
            except RentalError as rene:
                print(str(rene))


start_program = Start(ClientServices, MovieServices, RentalServices, UndoServices)
start_program.start_program()
