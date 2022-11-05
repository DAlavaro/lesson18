import pytest
from unittest.mock import MagicMock

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService

# from dao.model.genre import Genre
# from dao.model.director import Director


@pytest.fixture()
def movie_dao_fixture():
    movie_dao = MovieDAO(None)

    # d1 = Director(id=1, name='test')
    # g1 = Genre(id=1, name='test')
    #
    # red = Movie(
    #     id=1,
    #     title='one',
    #     description='рорено',
    #     trailer='qwerty',
    #     year=1984,
    #     rating=8,
    #     genre_id=1,
    #     director_id=1,
    #     genre=g1,
    #     director=d1
    # )



    joe = Movie(id=1, title='red', description='Шанкс', trailer='qwerty', year=1984, genre_id=1, director_id=1)
    nina = Movie(id=2, title='onepiece', description='Рорено', trailer='asdfg', year=2022, genre_id=2, director_id=2)

    # movie_dao.get_one = MagicMock(return_value=red)
    # movie_dao.get_all = MagicMock(return_value=[red, ])
    movie_dao.get_one = MagicMock(return_value=joe)
    movie_dao.get_all = MagicMock(return_value=[joe, nina])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_fixture):
        self.movie_service = MovieService(dao=movie_dao_fixture)

    # def test_partially_update(self):
    #     movie_d = {
    #         'id': 1,
    #         'year': 2020,
    #     }
    #     movie = self.movie_service.partially_update(movie_d)
    #     assert movie.year == 2020

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id == 1

    def test_get_all(self):
        movie = self.movie_service.get_all()

        assert movie is not None
        assert len(movie) == 2
        # assert len(movie) == 1

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
