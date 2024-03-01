from const import hash_password
from models.tables import User
from module.base import DAL

from sqlalchemy import select

# https://towardsdatascience.com/build-an-async-python-service-with-fastapi-sqlalchemy-196d8792fa08

class UserDAL(DAL):

    async def create_user(self,username:str,email:str,password:str):
        newUser=User(
            username= username,
            email= email,
            password= hash_password(password)
        ) # 填入table
        self.db.add(newUser)
        await self.db.flush()
    
    async def verify_password(self,username,password):
        
        query = await self.db.execute(select(User).where(User.username == username))
        resp :list[User] = query.scalars().all() # 正常來說只會有一筆
        if len(resp) == 0:
            return False
        if hash_password(password) == resp[0].password:
            # 登入成功
            return True
        return False # 密碼錯誤
    
    async def get_target_user_info(self,username):
        query = await self.db.execute(select(User).where(User.username == username))
        resp:list[User]= query.scalars().all() 
        if len(resp) == 0:
            return {}
        else:
            return {"username":resp[0].username,"email":resp[0].email,"level":resp[0].level}
