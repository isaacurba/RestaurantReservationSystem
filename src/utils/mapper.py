from src.dtos.user import UserCreate
from src.db_models.user import User


class Mapper:

    @staticmethod
    def map(self, user_data: UserCreate) -> User:
        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            password=user_data.password,
            is_active=user_data.is_active,
        )
        return user
