from src.dtos.user import UserLogin, UserResponse, UserCreate
from src.exceptions.user_already_exist_exception import UserAlreadyExistsException
from src.services.auth_service import AuthService
from utils.mapper import Mapper


class AuthServiceImpl(AuthService):

    def __init__(self, repository):
        self.repository = repository

    def register(self, user_data: UserCreate) -> UserResponse:
        existing_user = self.repository.find_by_email(user_data.email)
        if existing_user is not None:
            raise UserAlreadyExistsException(user_data.email)

        user = Mapper.map(self, user_data)
        saved_user = self.repository.save(user)
        return UserResponse.model_validate(saved_user)








    def login(self, user_data: UserLogin) -> UserResponse:
        pass