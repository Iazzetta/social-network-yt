from fastapi import HTTPException, Header
from src.datalayer.models.user import UserModel

async def verify_token(token: str = Header("Authorization")):
    user = await get_user_by_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Não autorizado.")
    return user

async def get_user_by_token(token):
    try:
        user = await UserModel.get(token=token)
        return user
    except Exception as e:
        return False

