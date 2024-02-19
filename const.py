import hashlib as hash

def hash_password(password:str)-> str:
    return hash.sha256(password.encode('utf-8')).hexdigest()