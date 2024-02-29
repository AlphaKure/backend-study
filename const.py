import hashlib as hash
import os
import datetime as dt
from typing import Literal

from jose import jwt,ExpiredSignatureError,JWTError
from fastapi import HTTPException

def jwt_encode(datas:dict):
    temp=datas.copy()
    temp["exp"] = dt.datetime.utcnow()+dt.timedelta(hours=int(os.getenv("TOKEN_EXPIRE_HOURS"))) # 設定token有效時長 exp不能改
    encoded_jwt = jwt.encode(temp,os.getenv("TOKEN_SECRET"))
    return encoded_jwt

def jwt_verify(token:str):
    try:
        payload = jwt.decode(token, os.getenv("TOKEN_SECRET"))
        return payload
    except ExpiredSignatureError:
        # token過期
        raise  HTTPException(
            status_code=401,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"}
        )
    except JWTError:
        # token 有誤
        return None

def hash_password(password:str)-> str:
    return hash.sha256(password.encode('utf-8')).hexdigest()