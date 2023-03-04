import unittest

from repository.Repository import Repository
from repository.RepoException import RepoError
from services.ClientService import ClientService
from services.RentalService import RentalService
from services.MovieService import MovieService
from services.RentalException import RentalError
from domain.Client import Client
from domain.Client import ClientValidator
from domain.Movie import Movie
from domain.Movie import MovieValidator
from domain.Rental import Rental
from domain.Rental import RentalValidator
from domain.ValidatorException import ValidatorError
import datetime
import copy


class ClientTest(unittest.TestCase):
    def setUp(self):
        self._movie = Movie(1, 2, 3, 4)
        self._client = Client(12345, "Cosmin")
        self._fail_client1 = Client(1234, "Andrei")
        self._fail_client2 = Client("idk", "Mihai")
        self._validator = ClientValidator()

    def test_property(self):
        self.assertEqual(self._client._client_id, int(self._client.id))
        self.assertEqual(self._client._name, self._client.name)

    def test_instance(self):
        self.assertIsInstance(self._client, Client)

    def test_str(self):
        self.assertEqual(str(self._client), "Client id is : 12345 and his name is : Cosmin")

    def test_repr(self):
        self.assertEqual(self._client, "Client id is : 12345 and his name is : Cosmin")

    def test_validator(self):
        self.assertRaises(ValidatorError, self._validator.validate, self._fail_client1)
        self.assertRaises(ValidatorError, self._validator.validate, self._fail_client2)
        self.assertRaises(TypeError, self._validator.validate, self._movie)

    def tearDown(self):
        self._movie = None
        self._client = None
        self._fail_client1 = None
        self._fail_client2 = None
        self._validator = None


class MovieTest(unittest.TestCase):
    def setUp(self):
        self._movie = Movie(123456, "title", "description", "Action")
        self._validator = MovieValidator()
        self._client = Client(1, 2)
        self._fail_movie1 = Movie(123456, "title", "description", "not genre")
        self._fail_movie2 = Movie("not integer", "title", "description", "Action")
        self._fail_movie3 = Movie(12345, "title", "description", "Action")

    def test_property(self):
        self.assertEqual(self._movie._movie_id, int(self._movie.id))
        self.assertEqual(self._movie._description, self._movie.description)
        self.assertEqual(self._movie._title, self._movie.title)
        self.assertEqual(self._movie._genre, self._movie.genre)

    def test_instance(self):
        self.assertIsInstance(self._movie, Movie)

    def test_str(self):
        self.assertEqual(str(self._movie),
                         "Movie name is : title (id is 123456) .Description : description. Genre is Action")

    def test_repr(self):
        self.assertEqual(self._movie,
                         "Movie name is : title (id is 123456) .Description : description. Genre is Action")

    def test_validator(self):
        self.assertRaises(TypeError, self._validator.validate, self._client)
        self.assertRaises(ValidatorError, self._validator.validate, self._fail_movie1)
        self.assertRaises(ValidatorError, self._validator.validate, self._fail_movie2)
        self.assertRaises(ValidatorError, self._validator.validate, self._fail_movie3)

    def tearDown(self):
        self._movie = None
        self._validator = None
        self._client = None
        self._fail_movie1 = None
        self._fail_movie2 = None
        self._fail_movie1 = None


class TestRental(unittest.TestCase):
    def setUp(self):
        self._rental = Rental(123, 123456, 12345, datetime.datetime(2021, 12, 1), datetime.datetime(2021, 12, 15), None)
        self._validator = RentalValidator()
        self._client = Client(1, 2)
        self._fail_rental1 = Rental("not integer", 123456, 12345, datetime.datetime(2021, 12, 1),
                                    datetime.datetime(2021, 12, 15), None)
        self._fail_rental2 = Rental(1234, 123456, 12345, datetime.datetime(2021, 12, 1),
                                    datetime.datetime(2021, 12, 15), None)

    def test_property(self):
        self.assertEqual(self._rental._rental_id, int(self._rental.id))
        self.assertEqual(self._rental._movie_id, int(self._rental.movie_id))
        self.assertEqual(self._rental._client_id, int(self._rental.client_id))
        self.assertEqual(self._rental._rented_date, self._rental.rented_date)
        self.assertEqual(self._rental._returned_date, self._rental.returned_date)
        self.assertEqual(self._rental._due_date, self._rental.due_date)

    def test_instance(self):
        self.assertIsInstance(self._rental, Rental)

    def test_setter(self):
        self._rental.returned_date = datetime.datetime(2021, 12, 2)
        self.assertEqual(self._rental.returned_date, datetime.datetime(2021, 12, 2))

    def test_str(self):
        self.assertEqual(str(self._rental), "Client id : 12345, Movie id : 123456, Rental id : 123, Rented date : "
                                            "2021-12-01 00:00:00, Due date : 2021-12-15 00:00:00, Returned date : "
                                            "None")

    def test_repr(self):
        self.assertEqual(self._rental, "Client id : 12345, Movie id : 123456, Rental id : 123, Rented date : "
                                       "2021-12-01 00:00:00, Due date : 2021-12-15 00:00:00, Returned date : "
                                       "None")

    def test_validator(self):
        self.assertRaises(TypeError, self._validator.validate, self._client)
        self.assertRaises(ValidatorError, self._validator.validate, self._fail_rental1)
        self.assertRaises(ValidatorError, self._validator.validate, self._fail_rental2)


class TestRepo(unittest.TestCase):
    def setUp(self):
        self._repo = Repository()
        self._repo.add(Client(1, 2))
        self._repo.add(Client(2, 3))

    def test_instance(self):
        self.assertIsInstance(self._repo, Repository)

    def test_property(self):
        self.assertEqual(self._repo._object_list, self._repo.object_list)

    def test_str(self):
        self.assertEqual(str(self._repo),
                         "Client id is : 1 and his name is : 2\nClient id is : 2 and his name is : 3\n")

    def test_add(self):
        self.assertRaises(RepoError, self._repo.add, Client(1, 2))

    def test_delete(self):
        test_list = copy.copy(self._repo.object_list)
        self.assertRaises(RepoError, self._repo.delete, Client(3, 4))
        test_client = Client(3, 4)
        self._repo.add(test_client)
        self._repo.delete(test_client)
        self.assertEqual(self._repo.object_list, test_list)

    def test_find_index(self):
        self.assertEqual(self._repo.find_index(Client(2, 3)), 1)

    def test_update(self):
        self.assertRaises(RepoError, self._repo.update, Client(8, 9))
        self._repo.update(Client(2, 4))

    def tearDown(self):
        self._repo = None


class TestValidatorError(unittest.TestCase):
    def setUp(self):
        self._message = ValidatorError(["idk"])

    def test_str(self):
        self.assertEqual(str(self._message), "idk\n")

    def tearDown(self):
        self._message = None


class TestRepoError(unittest.TestCase):
    def setUp(self):
        self._message = RepoError(["idk"])

    def test_str(self):
        self.assertEqual(str(self._message), "idk\n")

    def tearDown(self):
        self._message = None


class TestClientService(unittest.TestCase):
    def setUp(self):
        self._client_service = ClientService(Repository(), Repository(), ClientValidator())
        self._client_service.create(12345, "Cosmin")
        self._client_service._rental_repo.add(Rental(123, 123456, 12345, datetime.datetime(2021, 12, 1)
                                                     , datetime.datetime(2021, 12, 15), None))


    def test_delete(self):
        test_list = copy.copy(self._client_service._client_repo.object_list)
        self._client_service.create(12346,"Andrei")
        self._client_service.delete("12346")
        self.assertEqual(self._client_service._client_repo.object_list,test_list)

