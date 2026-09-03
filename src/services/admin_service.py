from abc import ABC, abstractmethod

from src.db_models.user import User
from src.schemas.menu_item import MenuItemResponse, MenuItemCreate, MenuItemUpdate


class AdminService(ABC):

    @abstractmethod
    def add_menu_item(self, user: User, item: MenuItemCreate) -> MenuItemResponse:
        pass

    @abstractmethod
    def remove_item(self, user: User, item_id: int) -> None:
        pass

    @abstractmethod
    def update_item(self, user: User, item_id: int, item: MenuItemUpdate) -> MenuItemResponse:
        pass