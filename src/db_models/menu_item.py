from sqlalchemy import Integer, String, Numeric, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.models.category import Category


class MenuItem(Base):
    __tablename__ = "menu_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    menu_id: Mapped[int] = mapped_column(ForeignKey("menus.id"),nullable=False)

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    category: Mapped[Category] = mapped_column(Enum(Category), nullable=False)

    description: Mapped[str] = mapped_column(String(255), nullable=False)

    menu = relationship("Menu", back_populates="menu_items")