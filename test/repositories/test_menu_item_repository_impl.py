import pytest

from database import SessionLocal
from src.db_models.menu import Menu
from src.db_models.menu_item import MenuItem
from src.models.category import Category
from src.repositories.menu_item_repository import MenuItemRepository
from src.repositories.menu_item_repository_impl import MenuItemRepositoryImpl

class TestMenuItemRepository:

    @pytest.fixture
    def session(self):
        session = SessionLocal()

        yield session

        session.query(MenuItem).delete()
        session.query(Menu).delete()
        session.commit()
        session.close()

    @pytest.fixture
    def repository(self, session) -> MenuItemRepository:
        return MenuItemRepositoryImpl(session)

    @pytest.fixture
    def menu(self, session):
        menu = Menu(
            name="Main Menu",
            description="Main restaurant menu"
        )

        session.add(menu)
        session.commit()
        session.refresh(menu)

        return menu


    @pytest.fixture
    def menu_item(self, menu):
        return MenuItem(
            menu_id=menu.id,
            name="coke",
            price=10.00,
            category=Category.DRINK,
            description="Cold coke"
        )

    def test_save_menu_item(self, repository, menu_item):
        saved = repository.save(menu_item)

        assert saved.id is not None
        assert saved.name == "coke"
        assert saved.price == 10.00
        assert saved.category == Category.DRINK
        assert saved.description == "Cold coke"

    def test_to_find_menu_item_by_id(self, repository, menu_item):
        saved = repository.save(menu_item)
        found = repository.find_by_id(saved.id)

        assert found is not None
        assert found.id == saved.id
        assert found.name == saved.name
        assert found.price == saved.price
        assert found.category == saved.category
        assert found.description == saved.description

    def test_to_find_menu_item_that_does_not_exist(self, repository, menu_item):
        found = repository.find_by_id(menu_item.id)
        assert found is None

    def test_to_find_all_menu_items(self, repository, menu, menu_item):
        saved = repository.save(menu_item)

        menu_item2 = MenuItem(
            menu_id=menu.id,
            name="meat",
            price=15.00,
            category=Category.PROTEIN,
            description="Beef burger"
        )

        saved2 = repository.save(menu_item2)
        items = repository.find_all()

        assert len(items) == 2
        assert any(item.id == saved.id for item in items)
        assert any(item.id == saved2.id for item in items)

    def test_to_find_empty_list_when_no_user_exist(self, repository, menu_item):
        saved = repository.find_all()
        assert saved == []

    def test_to_delete_menu_item(self, repository, menu_item):
        saved = repository.save(menu_item)
        repository.delete(saved.id)
        found = repository.find_by_id(saved.id)
        assert found is None
