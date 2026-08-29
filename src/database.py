from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "mysql+pymysql://root:52315678@localhost/restaurant_db"
engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass