from domain import ValidatorException


class Movie:
    """
    Movie class which holds the movie id ,its title ,description and genre
    """
    def __init__(self, movie_id, title, description, genre):
        self._movie_id = movie_id
        self._title = title
        self._description = description
        self._genre = genre

    def __str__(self):
        return "Movie name is : " + str(self._title) + " (id is " + str(self._movie_id) + ") .Description : " + str(
            self._description) + ". Genre is " + str(self._genre)

    def __repr__(self):
        return "Movie name is : " + str(self._title) + " (id is " + str(self._movie_id) + ") .Description : " + str(
            self._description) + ". Genre is " + str(self._genre)

    @property
    def id(self):
        return str(self._movie_id)

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def genre(self):
        return self._genre


class MovieValidator:
    def __init__(self):
        self._movie_genre_list = ["Action", "Comedy", "Romance", "Fantasy", "Drama", "Horror", "Mystery"]

    def validate(self, movie):
        if isinstance(movie, Movie) == False:
            raise TypeError(">can only validate movie objects")
        _errors = []
        if movie.genre not in self._movie_genre_list:
            _errors.append(">genre does not exist")
        if movie.id.isnumeric() is False:
            _errors.append(">client id must be an integer number")
        if len(movie.id) != 6:
            _errors.append("incorrect id format")
        if len(_errors) > 0:
            raise ValidatorException.ValidatorError(_errors)
