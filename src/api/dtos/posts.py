from pydantic import BaseModel

class PostCreation(BaseModel):
    message: str

class CommentCreation(BaseModel):
    message: str