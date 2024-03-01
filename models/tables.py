# db tables

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,Boolean,ForeignKey

Base = declarative_base()

class User(Base):

    __tablename__ = "user"
    username = Column(String(),nullable=False,unique=True,primary_key=True)
    password = Column(String(),nullable=False)
    email = Column(String(),nullable=False,unique=True)
    verified = Column(Boolean(),default=False,nullable=False)

class EmailVerified(Base):

    __tablename__ = "emailVerified"
    username = Column(String(),ForeignKey("user.username",ondelete="CASCADE"),unique=True,primary_key=True)
    token = Column(String(),nullable=False)
