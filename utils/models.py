# db tables

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,Integer,DateTime

Base = declarative_base()

class User(Base):

    __tablename__ = "user"
    username = Column(String(),nullable=False,unique=True,primary_key=True)
    password = Column(String(),nullable=False)
    email = Column(String(),nullable=False,unique=True)
    level = Column(Integer())