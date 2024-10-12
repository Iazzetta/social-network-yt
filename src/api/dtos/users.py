from pydantic import BaseModel

class UserRegistration(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str