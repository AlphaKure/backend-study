# db tables

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,Integer

Base = declarative_base()

class User(Base):

    __tablename__ = "user"
    id = Column(String(),primary_key=True)
    username = Column(String(),nullable=False,unique=True)
    password = Column(String(),nullable=False)
    email = Column(String(),nullable=False,unique=True)
    level = Column(Integer)

