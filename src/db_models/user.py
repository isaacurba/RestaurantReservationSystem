from sqlalchemy import String, Column, Integer, Boolean, Enum
from sqlalchemy.orm import Mapped

from src.database import Base
from src.models.user_role import UserRole


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = Column(String(100), nullable=False)
    email: Mapped[str] = Column(String(100), unique=True, nullable=False)
    password: Mapped[str] = Column(String(100), nullable=False)

    role: Mapped[UserRole] = Column(Enum(UserRole), default=UserRole.CUSTOMER, nullable=False)

    address: Mapped[str | None] = Column(String(200), nullable=True)

    is_active: Mapped[bool] = Column(Boolean, default=False, nullable=False)