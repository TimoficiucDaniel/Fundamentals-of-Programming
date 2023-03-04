from domain.Rental import Rental
from services.RentalException import RentalError
import datetime
from domain.Undo import UndoRedoActions
from domain.Undo import Parameter
from domain.Undo import UndoRedoCommandBlock


class RentalService:
    """
    rental service class that calls functions related to elements in the rental repo
    """

    def __init__(self, client_repo, movie_repo, rental_repo, validator):
        self._client_repo = client_repo
        self._movie_repo = movie_repo
        self._rental_repo = rental_repo
        self._validator = validator

    def delete(self, rental_id):
        for rentals in self._rental_repo.object_list:
            if rentals.id == rental_id:
                self._rental_repo.delete(rentals)

    def check_if_client_has_rented(self, client_id):
        """
        function that checks if the client can rent another movie
        :param client_id:
        :return:
        """
        for rentals in self._rental_repo.object_list:
            if client_id == rentals.client_id:
                if rentals.returned_date is None and datetime.datetime.now().date() > rentals.due_date.date():
                    return False
        return True

    def check_if_client_exists(self, client_id):
        """
        function that checks if a client with a certain id exists
        :param client_id:
        :return:
        """
        for clients in self._client_repo.object_list:
            if client_id == clients.id:
                return True
        return False

    def check_if_movie_exists(self, movie_id):
        """
        function that checks if a movie wit a certain id exists
        :param movie_id:
        :return:
        """
        for movies in self._movie_repo.object_list:
            if movie_id == movies.id:
                return True
        return False

    def create_rental(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        """
        function that creates a rental and validates it then calls the add function from the rental repo
        :param rental_id:
        :param movie_id:
        :param client_id:
        :param rented_date:
        :param due_date:
        :param returned_date:
        :return:
        """
        error_list = []
        if self.check_if_client_exists(client_id) is False:
            error_list.append(">client does not exist")
        if self.check_if_movie_exists(movie_id) is False:
            error_list.append(">movie does not exist")
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self._validator.validate(rental)
        if self.check_if_client_has_rented(client_id) is False:
            error_list.append(">client has already rented a movie and has yet to return it")
        if len(error_list) > 0:
            raise RentalError(error_list)
        block = UndoRedoCommandBlock()
        param = Parameter(str(rental_id), str(movie_id), str(client_id), rented_date, due_date, returned_date)
        action = UndoRedoActions('delete_rental', param)
        block.add_to_block(action)
        self._rental_repo.add(rental)
        return block

    def rental_returned(self, rental_id, returned_date):
        """
        function that updates a rental with a returned date when a movie is returned
        :param rental_id:
        :param returned_date:
        :return:
        """
        for rentals in self._rental_repo.object_list:
            if rental_id == rentals.id:
                if rentals.returned_date is not None:
                    raise RentalError([">this movie was already returned"])
                rentals.returned_date = returned_date

    def list(self):
        r = ""
        for rentals in self._rental_repo.object_list:
            for clients in self._client_repo.object_list:
                if clients.id == rentals.client_id:
                    name = clients.name
            for movies in self._movie_repo.object_list:
                if movies.id == rentals.movie_id:
                    movie_name = movies.title
            if rentals.returned_date is None:
                r += "Client named " + name + " has rented the movie " + movie_name + " on " + str(rentals.rented_date) \
                     + " and is yet to return it on " + str(rentals.due_date)
            else:
                r += "Client named " + name + " has rented the movie " + movie_name + " on " + str(rentals.rented_date) \
                     + " and has returned it on " + str(rentals.returned_date)
            r += "\n"
        return r

    def most_rented_movies(self):
        """
        a function that first creates a new list in which it inserts other lists given by the format
        [movie_id , how many days the movie has been rented for]
        then the function calculates the total days a movie has been rented for and stores the values in
        another list along with the movie id ;this list is then sorted by the days it has been rented for
        and from it a list containing the output that is to be printed is created and returned
        :return:
        """
        list_with_movie_ids_and_rented_time = []
        for rentals in self._rental_repo.object_list:
            if rentals.returned_date is None:
                date_dif = datetime.datetime.now().date() - rentals.rented_date.date()
                list_with_movie_ids_and_rented_time.append([rentals.movie_id, date_dif.days])
            else:
                date_dif = rentals.returned_date.date() - rentals.rented_date.date()
                list_with_movie_ids_and_rented_time.append([rentals.movie_id, date_dif.days])
        new_list = []
        for i in range(len(list_with_movie_ids_and_rented_time)):
            day_sum = 0
            for elements in list_with_movie_ids_and_rented_time:
                if list_with_movie_ids_and_rented_time[i][0] == elements[0]:
                    day_sum = day_sum + elements[1]
            new_list.append([list_with_movie_ids_and_rented_time[i][0], day_sum])
        new_list.sort(key=lambda x: x[1], reverse=True)
        print_list = []
        index = 1
        for i in range(len(new_list)):
            if i == 0:
                for elements in self._movie_repo.object_list:
                    if elements.id == new_list[0][0]:
                        print_list.append(
                            str(index) + ".Movie: " + elements.title + " with id: " + elements.id + " has " +
                            str(new_list[0][1]) + " rented days.")
                        index += 1
            else:
                if new_list[i][0] != new_list[i - 1][0]:
                    for elements in self._movie_repo.object_list:
                        if elements.id == new_list[i][0]:
                            print_list.append(
                                str(index) + ".Movie: " + elements.title + " with id: " + elements.id + " has " +
                                str(new_list[i][1]) + " rented days.")
                            index += 1
        return print_list

    def most_active_client(self):
        """
        a function that first creates a new list in which it inserts other lists given by the format
        [client_id , how many days the client has rented ]
        then the function calculates the total days a client has rented and stores the values in another list along
        with the client id; this list is then sorted by the amount of rented days and from it a list containing the
        output that is to be printed is created and returned
        :return:
        """
        list_with_client_ids_and_rented_time = []
        for rentals in self._rental_repo.object_list:
            if rentals.returned_date is None:
                date_dif = datetime.datetime.now().date() - rentals.rented_date.date()
                list_with_client_ids_and_rented_time.append([rentals.client_id, date_dif.days])
            else:
                date_dif = rentals.returned_date.date() - rentals.rented_date.date()
                list_with_client_ids_and_rented_time.append([rentals.client_id, date_dif.days])
        new_list = []
        for i in range(len(list_with_client_ids_and_rented_time)):
            day_sum = 0
            for elements in list_with_client_ids_and_rented_time:
                if list_with_client_ids_and_rented_time[i][0] == elements[0]:
                    day_sum = day_sum + elements[1]
            new_list.append([list_with_client_ids_and_rented_time[i][0], day_sum])
        new_list.sort(key=lambda x: x[1], reverse=True)
        print_list = []
        index = 1
        for i in range(len(new_list)):
            if i == 0:
                for elements in self._client_repo.object_list:
                    if elements.id == new_list[0][0]:
                        print_list.append(
                            str(index) + ".Name: " + elements.name + " with id: " + elements.id + " has " +
                            str(new_list[0][1]) + " rented days.")
                        index += 1
            else:
                if new_list[i][0] != new_list[i - 1][0]:
                    for elements in self._client_repo.object_list:
                        if elements.id == new_list[i][0]:
                            print_list.append(
                                str(index) + ".Name: " + elements.name + " with id: " + elements.id + " has " +
                                str(new_list[i][1]) + " rented days.")
                            index += 1
        return print_list

    def late_rentals(self):
        """
        a function that creates a list which itself contains other lists given by the format
        [movie_id, days the movie has been rented for, client id that rented movie]
        then this list is sorted by the amount of days the movie has been rented for
        and from it the output is generated and returned
        :return:
        """
        list_with_rentals_ids_and_rented_time = []
        for rentals in self._rental_repo.object_list:
            if rentals.returned_date is None:
                if datetime.datetime.now().date() > rentals.due_date.date():
                    date_dif = datetime.datetime.now().date() - rentals.rented_date.date()
                    list_with_rentals_ids_and_rented_time.append([rentals.movie_id, date_dif.days, rentals.client_id])
        list_with_rentals_ids_and_rented_time.sort(key=lambda x: x[1], reverse=True)
        index = 1
        print_list = []
        for i in range(len(list_with_rentals_ids_and_rented_time)):
            for elements in self._movie_repo.object_list:
                if elements.id == list_with_rentals_ids_and_rented_time[i][0]:
                    print_list.append(
                        str(index) + ".Movie: " + elements.title + " with id: " + elements.id + " has been rented for " +
                        str(list_with_rentals_ids_and_rented_time[i][1]) + " days by client with id: " +
                        str(list_with_rentals_ids_and_rented_time[i][2]))
                    index += 1
        return print_list
