from domain.Movie import Movie
from domain.Undo import UndoRedoActions
from domain.Undo import Parameter
from domain.Undo import UndoRedoCommandBlock


class MovieService:
    """
        movie service class used to call functions that create,delete,read,update in the movie repo
        """

    def __init__(self, movie_repo, rental_repo, validator):
        self._rental_repo = rental_repo
        self._movie_repo = movie_repo
        self._validator = validator

    def add(self, movie_id, title, description, genre):
        """
        function that creates a new object based on the parameters,validates it
                and calls the add function from the repo with this new object
        :param movie_id:
        :param title:
        :param description:
        :param genre:
        :return:
        """
        block = UndoRedoCommandBlock()

        movie = Movie(movie_id, title, description, genre)
        self._validator.validate(movie)
        param = Parameter(str(movie_id), title, description, genre, None, None)
        actions = UndoRedoActions('delete_movie', param)
        block.add_to_block(actions)
        self._movie_repo.add(movie)
        return block

    def delete(self, movie_id):
        """
        function that deletes a movie from the movie repo and then deletes all rentals related to that movie
        :param movie_id:
        :return:
        """
        block = UndoRedoCommandBlock()
        aux = False
        for movies in self._movie_repo.object_list:
            if movie_id == movies.id:
                self._movie_repo.delete(movies)
                id = movies.id
                title = movies.title
                description = movies.description
                genre = movies.genre
                param = Parameter(str(id), title, description, genre, None, None)
                action = UndoRedoActions('create_movie', param)
                block.add_to_block(action)
                aux = True
        for rentals in self._rental_repo.object_list:
            if movie_id == rentals.movie_id:
                self._rental_repo.delete(rentals)
                id1 = rentals.id
                id2 = rentals.movie_id
                id3 = rentals.client_id
                rented_date = rentals.rented_date
                due_date = rentals.due_date
                returned_date = rentals.returned_date
                param = Parameter(str(id1), str(id2), str(id3), rented_date, due_date, returned_date)
                action = UndoRedoActions('create_rental', param)
                block.add_to_block(action)
        if aux is False:
            raise ValueError("No movie to delete")
        return block

    def update(self, movie_id, title, description, genre):
        """
        function that creates a new object with the same id as the one to be updated and then calls the
         update function from repo with this new object with updated data
        :param movie_id:
        :param title:
        :param description:
        :param genre:
        :return:
        """
        block = UndoRedoCommandBlock()
        movie = Movie(movie_id, title, description, genre)
        self._validator.validate(movie)
        for movies in self._movie_repo.object_list:
            if movies.id == movie_id:
                id = movies.id
                title = movies.title
                description = movies.description
                genre = movies.genre
                param = Parameter(str(id), title, description, genre, None, None)
                action = UndoRedoActions('update_movie', param)
                block.add_to_block(action)
        self._movie_repo.update(movie)
        return block

    def list(self):
        return str(self._movie_repo)

    def search_by_title(self, user_input):
        user_input = user_input.strip()
        new_list = []
        for movies in self._movie_repo.object_list:
            if user_input.lower() in movies.title.lower():
                new_list.append(movies)
        return new_list

    def search_by_id(self, user_input):
        user_input = user_input.strip()
        new_list = []
        for movies in self._movie_repo.object_list:
            if user_input == movies.id:
                new_list.append(movies)
        return new_list

    def search_by_description(self, user_input):
        user_input = user_input.strip()
        new_list = []
        for movies in self._movie_repo.object_list:
            if user_input.lower() in movies.description.lower():
                new_list.append(movies)
        return new_list

    def search_by_genre(self, user_input):
        user_input = user_input.strip()
        new_list = []
        for movies in self._movie_repo.object_list:
            if user_input.lower() in movies.genre.lower():
                new_list.append(movies)
        return new_list
