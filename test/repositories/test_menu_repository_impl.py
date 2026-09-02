import pytest

from src.database import SessionLocal
from src.db_models.menu import Menu
from src.db_models.menu_item import MenuItem
from src.repositories.menu_repository_impl import MenuRepositoryImpl


class TestMenuRepository:

    @pytest.fixture
    def session(self):
        session = SessionLocal()

        yield session

        session.query(Menu).delete()
        session.commit()
        session.close()

    @pytest.fixture
    def repository(self, session):
        return MenuRepositoryImpl(session)

    @pytest.fixture
    def menu(self):
        return Menu(
            name="Main menu",
            description="Main menu description",
        )

    def test_save_menu(self, repository, menu):
        saved = repository.save(menu)

        assert saved.id is not None
        assert saved.name == "Main menu"
        assert saved.description == "Main menu description"

    def test_save_and_find_menu_by_id(self, repository, menu):
        saved = repository.save(menu)
        found = repository.find_by_id(saved.id)

        assert found.id is not None
        assert found.name == saved.name
        assert found.description == saved.description

    def test_find_by_id_that_doesnt_exist(self, repository, menu):
        found = repository.find_by_id(9999999)
        assert found is None

    def test_to_find_all(self, repository, menu):
        saved = repository.save(menu)
        menu_items = repository.find_all()
        assert len(menu_items) == 1
        assert menu_items[0].name == saved.name
        assert menu_items[0].description == saved.description

    def test_to_delete_menu(self, repository, menu):
        saved = repository.save(menu)
        repository.delete(saved.id)
        found = repository.find_by_id(saved.id)
        assert found is None