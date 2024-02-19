from utils import sessions
from utils.schemas import UserCreate
from module import UserDAL

from fastapi import APIRouter,Request,Depends

route = APIRouter(
    tags=['User']
)
# Depend
async def get_db():
    async with sessions() as session:
        async with session.begin():
            yield UserDAL(session)

@route.post('/user/register')
async def user_register(req:Request,reqBody:UserCreate,db:UserDAL=Depends(get_db)):
    """
    # 使用者註冊

    ## request body:
    - username (str): 帳號
    - password (str): 密碼
    - email (str): 信箱  
    """
    return await db.create_user(
        username= reqBody.username,
        email= reqBody.email,
        password= reqBody.password
    )