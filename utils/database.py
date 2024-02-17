# connect database

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

DB_URL = r'sqlite:///database.db'

engine = create_engine(
    url=DB_URL,
    connect_args={"check_same_thread": False} # For sqlite
)

session = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)
