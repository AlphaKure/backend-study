# db tables

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,Boolean,ForeignKey

Base = declarative_base()

class User(Base):

    __tablename__ = "account"
    username = Column(String(),nullable=False,unique=True,primary_key=True)
    password = Column(String(),nullable=False)
    email = Column(String(),nullable=False,unique=True)
    verified = Column(Boolean(),default=False,nullable=False)



