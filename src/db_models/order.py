from sqlalchemy import Integer, ForeignKey, Numeric, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.models.order_status import OrderStatus


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    total_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus), default=OrderStatus.PENDING, nullable=False)

    order_items = relationship("OrderItem", back_populates="order")