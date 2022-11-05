import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao_fixture():
    director_dao = DirectorDAO(None)

    joe = Director(id=1, name='Joe')
    nina = Director(id=2, name='Nina')

    director_dao.get_one = MagicMock(return_value=joe)
    director_dao.get_all = MagicMock(return_value=[joe, nina])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao_fixture):
        self.director_service = DirectorService(dao=director_dao_fixture)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id == 1

    def test_get_all(self):
        director = self.director_service.get_all()

        assert director is not None
        assert len(director) == 2

    def test_create(self):
        director_d = {
            'name': 'Rose'
        }

        director = self.director_service.create(director_d)

        assert director.id is not None

    def test_update(self):
        director_d = {
            'id': 1,
            'name': 'Rose'
        }

        self.director_service.update(director_d)

    def test_delete(self):
        self.director_service.delete(1)
