from pydantic import BaseModel
from fastapi import HTTPException

def login_wrong_exception():
    raise HTTPException(status_code=404, detail="E-mail/senha incorretos")

def email_already_exists():
    raise HTTPException(status_code=400, detail="E-mail ja cadastrado")