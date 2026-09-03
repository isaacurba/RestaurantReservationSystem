from abc import ABC, abstractmethod

from src.db_models.menu_item import MenuItem


class MenuItemRepository(ABC):

    @abstractmethod
    def save(self, item: MenuItem) -> MenuItem:
        pass

    @abstractmethod
    def find_by_id(self, item_id: int) -> MenuItem | None:
        pass
    @abstractmethod
    def find_by_name(self, name: str) -> MenuItem | None:
        pass

    @abstractmethod
    def find_all(self) -> list[MenuItem]:
        pass

    @abstractmethod
    def delete(self, item_id: int) -> None:
        pass

