import pytest
from unittest.mock import MagicMock

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService
from dao.model.genre import Genre
from dao.model.director import Director


@pytest.fixture()
def movie_dao_fixture():
    movie_dao = MovieDAO(None)


    luxury = Movie(
        id=21, title="Title22",
        description="Description22", trailer="Trailer22",
        year=2022, rating=4.8,
        genre_id=4, director_id=6)
    singing_city = Movie(
        id=22, title="Title23",
        description="Description23", trailer="Trailer23",
        year=2023, rating=4.1,
        genre_id=7, director_id=12)

    movie_dao.get_one = MagicMock(return_value=luxury)
    movie_dao.get_all = MagicMock(return_value=[luxury, singing_city])
    movie_dao.create = MagicMock(return_value=Movie(id=22))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_fixture):
        self.movie_service = MovieService(dao=movie_dao_fixture)

    def test_partially_update(self):
        movie_d = {
            'id': 1,
            'year': 2020
        }

        movie = self.movie_service.partially_update((movie_d))
        assert movie.year == movie_d.get('year')

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id == 21

    def test_get_all(self):
        movie = self.movie_service.get_all()

        assert movie is not None
        assert len(movie) == 2

    def test_create(self):
        movie_d = {
            'name': 'Rose'
        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_update(self):
        movie_d = {
            'id': 1,
            'name': 'Rose'
        }

        self.movie_service.update(movie_d)

    def test_delete(self):
        self.movie_service.delete(1)
