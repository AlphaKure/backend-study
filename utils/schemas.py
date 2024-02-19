# AKA Requests Body

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    email: str 
    password: str