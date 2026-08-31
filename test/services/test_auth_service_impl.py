import pytest

from src.database import SessionLocal
from src.db_models.user import User
from src.dtos.user import UserCreate
from src.exceptions.user_already_exist_exception import UserAlreadyExistsException
from src.models.user_role import UserRole
from src.repositories.user_repository_impl import UserRepositoryImpl
from src.services.auth_service_impl import AuthServiceImpl

class TestAuthServiceImpl:

    @pytest.fixture
    def session(self):
        session = SessionLocal()

        yield session

        session.query(User).delete()
        session.commit()
        session.close()

    @pytest.fixture
    def repository(self, session):
        return UserRepositoryImpl(session)

    @pytest.fixture
    def service(self, repository):
        return AuthServiceImpl(repository)

    @pytest.fixture
    def user_data(self):
        return UserCreate(
            full_name="Isaac Urban",
            email="isaac@mail.com",
            password="password",
            role=UserRole.CUSTOMER,
            is_active=False,
        )

    def test_register_user(self, service, user_data):
        result = service.register(user_data)
        assert result.email == "isaac@mail.com"
        assert result.full_name == "Isaac Urban"

    def test_register_user_already_exists(self, service, user_data):
        service.register(user_data)
        with pytest.raises(UserAlreadyExistsException):
            service.register(user_data)