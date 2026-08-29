from sqlalchemy import Integer, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)

    menu_item_id: Mapped[int] = mapped_column(ForeignKey("menu_items.id"), nullable=False)

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    order = relationship("Order", back_populates="order_items")

    menu_item = relationship("menu_items")