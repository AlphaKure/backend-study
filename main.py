import utils
from routers import user_route

from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def liftspan(app:FastAPI):
    await utils.init_db() # startup
    yield
    await utils.close_db() # close 

app = FastAPI(
    title="Backend-Study",
    version="0.0.3",
    lifespan=liftspan,
    openapi_tags=[
        {"name":"user"},{"name":"auth"},{"name":"ping"}
    ]
)

app.include_router(user_route)

@app.get('/',tags=['ping'])
def greeting():
    return "Hello"



