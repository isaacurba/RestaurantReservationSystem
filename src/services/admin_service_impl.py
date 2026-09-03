from src.exceptions.menu_item_not_found_exception import MenuItemNotFoundException
from src.exceptions.duplicate_menu_item_exception import DuplicateMenuItemException
from src.exceptions.forbidden_exception import ForbiddenException
from src.db_models.menu_item import MenuItem
from src.db_models.user import User
from src.models.user_role import UserRole
from src.schemas.menu_item import MenuItemResponse, MenuItemCreate, MenuItemUpdate
from src.services.admin_service import AdminService
from src.utils.mapper import Mapper


class AdminServiceImpl(AdminService):

    def __init__(self, repository):
        self.repository = repository

    def add_menu_item(self,user: User,item: MenuItemCreate) -> MenuItemResponse:

        if user.role != UserRole.ADMIN or not user.is_active:
            raise ForbiddenException("Only admins can add menu items")
        existing_menu_item = self.repository.find_by_name(item.name)

        if existing_menu_item is not None:
            raise DuplicateMenuItemException(f"Menu item with name {item.name} already exists")
        menu_item = Mapper.map_to_menu_item(item)
        saved_item = self.repository.save(menu_item)

        return MenuItemResponse.model_validate(saved_item)

    def remove_item(self, user: User, item_id: int) -> None:

        if user.role != UserRole.ADMIN or not user.is_active:
            raise ForbiddenException("Only admins can remove menu items")
        existing_item = self.repository.find_by_id(item_id)

        if existing_item is None:
            raise MenuItemNotFoundException(f"Menu item with id {item_id} not found")

        self.repository.delete(item_id)

    def update_item(self, user: User, item_id: int, item: MenuItemUpdate) -> MenuItemResponse:

        if user.role != UserRole.ADMIN or not user.is_active:
            raise ForbiddenException("Only admins can update menu items")

        existing_item = self.repository.find_by_id(item_id)
        if existing_item is None:
            raise MenuItemNotFoundException(f"Menu item with id {item_id} not found")

        updated_item = Mapper.map_to_update_menu_item(existing_item, item)
        saved_item = self.repository.save(updated_item)

        return MenuItemResponse.model_validate(saved_item)