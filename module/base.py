from sqlalchemy.orm import Session

class DAL:

    def __init__(self,db:Session) -> None:
        self.db = db