from utils import sessions
from utils.schemas import UserCreate,Auth
from module import UserDAL

from fastapi import APIRouter,Request,Depends
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

route = APIRouter()

# Depend
async def get_db():
    async with sessions() as session:
        async with session.begin():
            yield UserDAL(session)

@route.post('/user/register',
            tags=['user'],
            responses={
                200:{"description":"Request Accept","content":{"application/json":{"example":{"response":"success"}}}},
                400:{"description":"Request Reject","content":{"application/json":{"example":{"response":"email or username used!"}}}}
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
        return JSONResponse(content= {"response":"email or username used!"}, status_code=400)
    return JSONResponse(content= {"response":"success"}, status_code=200)

@route.post('/auth',tags=['auth'],responses={200:{"description":"Request Accept","content":{"application/json":{"example":{"response":True}}}}})
async def auth(req:Request,reqBody:Auth,db:UserDAL=Depends(get_db)):
    """
    # 使用者登入
    
    測試用，沒有實際用途

    ## request body:
    - username (str): 帳號
    - password (str): 密碼
    """
    return JSONResponse(content={"response":await db.verify_password(reqBody.username,reqBody.password)},status_code=200)