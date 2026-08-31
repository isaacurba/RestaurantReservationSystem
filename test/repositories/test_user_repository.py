import pytest

from src.database import SessionLocal
from src.db_models.user import User
from src.models.user_role import UserRole
from src.repositories.user_repository_impl import UserRepositoryImpl


class TestUserRepository:

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
    def user(self):
        return User(
            full_name="Isaac Urban",
            email="isaac@mail.com",
            password="password",
            role=UserRole.CUSTOMER,
            is_active=False,
        )

    def test_save_user(self, repository, user, session):
        saved_user = repository.save(user)

        assert saved_user.id is not None
        assert saved_user.full_name == "Isaac Urban"
        assert saved_user.email == "isaac@mail.com"

        database_user = session.get(User, saved_user.id)

        assert database_user is not None
        assert database_user.email == "isaac@mail.com"

    def test_find_user_by_id(self, repository, user):
        saved_user = repository.save(user)

        found_user = repository.find_by_id(saved_user.id)

        assert found_user is not None
        assert found_user.id == saved_user.id
        assert found_user.email == "isaac@mail.com"

    def test_find_user_by_id_returns_none_when_user_does_not_exist(self, repository):
        found_user = repository.find_by_id(999999)

        assert found_user is None

    def test_find_user_by_email(self, repository, user):
        repository.save(user)

        found_user = repository.find_by_email("isaac@mail.com")

        assert found_user is not None
        assert found_user.email == "isaac@mail.com"
        assert found_user.full_name == "Isaac Urban"

    def test_find_user_by_email_returns_none_when_user_does_not_exist(self, repository):
        found_user = repository.find_by_email("doesnotexist@mail.com")
        assert found_user is None

    def test_find_all_users(self, repository, user):
        user2 = User(
            full_name="John Doe",
            email="john@mail.com",
            password="password",
            role=UserRole.CUSTOMER,
            is_active=False,
        )

        repository.save(user)
        repository.save(user2)

        users = repository.find_all()

        assert len(users) == 2
        assert any(user.email == "isaac@mail.com" for user in users)
        assert any(user.email == "john@mail.com" for user in users)

    def test_find_all_users_returns_empty_list_when_no_users_exist(self, repository):
        users = repository.find_all()
        assert users == []

    def test_delete_user(self, repository, user):
        saved_user = repository.save(user)

        repository.delete(saved_user.id)
        found_user = repository.find_by_id(saved_user.id)
        assert found_user is None

    def test_delete_user_that_does_not_exist(self, repository):
        repository.delete(999999)

        found_user = repository.find_by_id(999999)
        assert found_user is None