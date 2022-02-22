
from pydantic import BaseModel, EmailStr


class UserBaseModel(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserInDB(BaseModel):
    hashed_password: str

class UserIn(UserBaseModel):
    password: str
  
class UserOut(BaseModel):
    pass


__all__ = ['UserInModel', 'UserOutModel', "UserDBModel"]
