from sqlalchemy import select

from src.db_models.menu_item import MenuItem
from src.repositories.menu_item_repository import MenuItemRepository


class MenuItemRepositoryImpl(MenuItemRepository):

    def __init__(self, session):
        self.session = session

    def save(self, item: MenuItem) -> MenuItem:
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item

    def find_by_id(self, item_id: int) -> MenuItem | None:
        return self.session.get(MenuItem, item_id)

    def find_by_name(self, name: str) -> MenuItem | None:
        statement = select(MenuItem).where(MenuItem.name == name)
        return self.session.scalar(statement)

    def find_all(self) -> list[MenuItem]:
        statement = select(MenuItem)
        return list(self.session.scalars(statement).all())

    def delete(self, item_id: int) -> None:
        menu_item = self.session.get(MenuItem, item_id)

        if menu_item is not None:
            self.session.delete(menu_item)
            self.session.commit()