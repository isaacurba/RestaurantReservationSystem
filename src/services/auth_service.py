from abc import ABC, abstractmethod

from src.dtos.user import UserCreate, UserLogin, UserResponse


class AuthService(ABC):

    @abstractmethod
    def register(self, user_data: UserCreate) -> UserResponse:
        pass

    @abstractmethod
    def login(self, user_data: UserLogin) -> UserResponse:
        pass

