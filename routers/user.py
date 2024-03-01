from utils import sessions
from utils.schemas import UserCreate
from routers.auth import decode_token
from module import UserDAL

from fastapi import APIRouter,Request,Depends,HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

route = APIRouter(
    prefix='/user',
    tags=['user']
)

# Depend
async def get_db():
    async with sessions() as session:
        async with session.begin():
            yield UserDAL(session)

@route.post('/register',
    responses={
        200:{"description":"Request Accept","content":{"application/json":{"example":{"detail":"success"}}}},
        400:{"description":"Request Reject","content":{"application/json":{"example":{"detail":"email or username used!"}}}}
        }
    )
async def user_register(req:Request,reqBody:UserCreate,db:UserDAL=Depends(get_db)):
    """
    # 使用者註冊

    ## request body:
    - username (str): 帳號
    - password (str): 密碼
    - email (str): 信箱  
    """
    try:
        await db.create_user(
            username= reqBody.username,
            email= reqBody.email,
            password= reqBody.password
        )
    except IntegrityError :
        raise HTTPException(status_code=400,detail="Username or email used!")
    return JSONResponse(content= {"detail":"success"}, status_code=200)

@route.get(
    '/',
    responses={
        200:{"description":"Request Accept","content":{"application/json":{"example":{"username":"username","email":"user@email.com","level":0}}}}
    }
)
async def get_current_user(datas:dict=Depends(decode_token),db:UserDAL=Depends(get_db)):
    """

    獲得目前登入帳號的基本資料

    Returns:
     - username (str) 使用者帳號
     - email (str) 使用者電子信箱
     - level (int) 等級
    """
    return await db.get_target_user_info(datas.get("username"))