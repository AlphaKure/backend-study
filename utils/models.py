# db tables

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,Integer,DateTime

Base = declarative_base()

class User(Base):

    __tablename__ = "user"
    id = Column(String(),primary_key=True)
    username = Column(String(),nullable=False,unique=True)
    password = Column(String(),nullable=False)
    email = Column(String(),nullable=False,unique=True)
    level = Column(Integer)


class Auth(Base):

    __tablename__ = "auth"
    username = Column(String(),primary_key=True)
    token = Column(String(),nullable=False)
    expireTime = Column(DateTime())

class BlackList(Base):

    __tablename__ = "blacklist"
    host = Column(String(),primary_key=True)
    times = Column(Integer(),nullable=False)
    lastTime = Column(DateTime())