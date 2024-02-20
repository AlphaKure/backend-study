from const import hash_password
from utils.models import User

import uuid
from sqlalchemy import select
from sqlalchemy.orm import Session

# https://towardsdatascience.com/build-an-async-python-service-with-fastapi-sqlalchemy-196d8792fa08

class UserDAL:

    def __init__(self,db:Session) -> None:
        self.db = db

    async def create_user(self,username:str,email:str,password:str):
        newUser=User(
            username= username,
            email= email,
            password= hash_password(password),
            id= str(uuid.uuid4()),
            level= 0
        ) # 填入table
        self.db.add(newUser)
        await self.db.flush()
    
    async def verify_password(self,username,password):
        
        query = await self.db.execute(select(User).where(User.username == username))
        resp = query.scalars().all() # 正常來說只會有一筆
        if len(resp) == 0:
            return False # 沒有這筆帳號
        if hash_password(password) == resp[0].password:
            return True # 密碼正確
        return False # 密碼錯誤