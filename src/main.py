from src.database import engine
from src.database import Base
from src.db_models.user import User
from src.db_models.menu import Menu
from src.db_models.menu_item import MenuItem
from src.db_models.order import Order
from src.db_models.order_item import OrderItem

Base.metadata.create_all(bind=engine)
print("Database tables created successfully")