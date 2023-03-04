from domain.ValidatorException import ValidatorError


class Rental:
    """
    Rental class which holds rentals (relation between clients and movies)
    """

    def __init__(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        self._rental_id = rental_id
        self._movie_id = movie_id
        self._client_id = client_id
        self._rented_date = rented_date
        self._due_date = due_date
        self._returned_date = returned_date

    @property
    def id(self):
        return str(self._rental_id)

    @property
    def movie_id(self):
        return str(self._movie_id)

    @property
    def client_id(self):
        return str(self._client_id)

    @property
    def rented_date(self):
        return self._rented_date

    @property
    def due_date(self):
        return self._due_date

    @property
    def returned_date(self):
        return self._returned_date

    @returned_date.setter
    def returned_date(self, value):
        self._returned_date = value

    def __str__(self):
        return "Client with name : " + str(self._) + ", Movie id : " + str(self._movie_id) + ", Rental id : " +\
               str(self._rental_id) + ", Rented date : " + str(self._rented_date) + ", Due date : " + \
               str(self._due_date) + ", Returned date : " + str(self._returned_date)
    def __repr__(self):
        return "Client id : " + str(self._client_id) + ", Movie id : " + str(self._movie_id) + ", Rental id : " + \
               str(self._rental_id) + ", Rented date : " + str(self._rented_date) + ", Due date : " + \
               str(self._due_date) + ", Returned date : " + str(self._returned_date)

class RentalValidator:
    @staticmethod
    def validate(rental):
        if isinstance(rental, Rental) == False:
            raise TypeError(">can only validate rental objects")
        _error_list = []
        if rental.id.isnumeric() is False:
            _error_list.append(">id has to be an integer")
        if len(rental.id) != 3:
            _error_list.append(">incorrect id format")
        if len(_error_list) > 0:
            raise ValidatorError(_error_list)
