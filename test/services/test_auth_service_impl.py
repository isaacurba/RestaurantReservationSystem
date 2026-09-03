import pytest

from src.exceptions import AppException
from src.database import SessionLocal
from src.db_models.user import User
from src.schemas.user import UserCreate, UserLogin
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
            address="address",
            role=UserRole.CUSTOMER,
            is_active=False,
        )
    @pytest.fixture
    def user_login_data(self):
        return UserLogin(
            email="isaac@mail.com",
            password="password",
        )

    def test_register_user(self, service, user_data):
        result = service.register(user_data)
        assert result.email == "isaac@mail.com"
        assert result.full_name == "Isaac Urban"

    def test_register_user_already_exists(self, service, user_data):
        service.register(user_data)
        with pytest.raises(AppException):
            service.register(user_data)

    def test_register_and_login_user(self, service, user_data, user_login_data):
        service.register(user_data)
        result = service.login(user_login_data)
        assert result.email == "isaac@mail.com"
        assert result.full_name == "Isaac Urban"
        assert result.is_active is True

    def test_register_and_login_with_invalid_credentials(self, service, user_data, user_login_data):
        service.register(user_data)
        login_data = UserLogin(
            email="isaac@mail.com",
            password="wrongpassword",
        )
        with pytest.raises(AppException):
            service.login(login_data)
