from src.db_models.user import User
from src.repositories.user_repository import UserRepository
from sqlalchemy import select


class UserRepositoryImpl(UserRepository):

    def __init__(self, session):
        self.session = session

    def save(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def find_by_id(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def find_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return self.session.scalar(statement)

    def find_all(self) -> list[User]:
        statement = select(User)
        return list(self.session.scalars(statement).all())

    def delete(self, user_id: int) -> None:
        user = self.session.get(User, user_id)

        if user is not None:
            self.session.delete(user)
            self.session.commit()