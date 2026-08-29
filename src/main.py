from src.database import engine
from src.database import Base
from src.db_models.user import User

Base.metadata.create_all(bind=engine)
print("Database tables created successfully")