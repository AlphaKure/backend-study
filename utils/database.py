# connect database

import os

from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession

load_dotenv()
DB_URL=os.getenv("DB_URL")

engine = create_async_engine(
    url=DB_URL,
    future=True,
    echo=True
)
#connect_args={"check_same_thread": False} # For sqlite

sessions = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
