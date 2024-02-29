from utils import sessions
from const import jwt_encode,jwt_verify
from module import UserDAL

from fastapi import APIRouter,Request,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm 

route = APIRouter(
    prefix='/auth',
    tags=['auth']
)

oauth2_token_scheme = OAuth2PasswordBearer(tokenUrl="/auth")

# Depends
async def get_db():
    async with sessions() as session:
        async with session.begin():
            yield UserDAL(session)

def decode_token(token:str=Depends(oauth2_token_scheme)):

    datas=jwt_verify(token)
    if datas:
        return datas
    else:
        raise HTTPException(status_code=401,detail="Incorrect token",headers={"WWW-Authenticate": "Bearer"})

@route.post("/")
async def auth(req:Request,form:OAuth2PasswordRequestForm=Depends(),db:UserDAL=Depends(get_db)):
    """
    # 使用者登入

    ## 使用OAuth表單

    ### Responses

    - access_token: str
    - token_type: str
    
    """
    isAccess = await db.verify_password(username=form.username,password=form.password)
    if isAccess:
        access = jwt_encode({"username":form.username})
        return {
            "access_token": access,
            "token_type": "bearer",
        }
    else:
        raise HTTPException(status_code=401,detail="Incorrect username or password",headers={"WWW-Authenticate": "Bearer"})

    