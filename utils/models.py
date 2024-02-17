# db tables

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,Integer

Base = declarative_base()

class User(Base):

    __tablename__='user'
    id = Column(Integer,primary_key=True)
    name =Column(String(100),nullable=False)
