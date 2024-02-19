from utils.database import engine,sessions
from utils.models import Base

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def close_db():
    async with engine.begin() as conn:
        await conn.close()