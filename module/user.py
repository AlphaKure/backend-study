from const import hash_password
from utils.models import User

import uuid

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
        )
        self.db.add(newUser)
        await self.db.flush()