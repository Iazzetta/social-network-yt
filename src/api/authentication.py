from functools import wraps
from fastapi import HTTPException
from src.datalayer.models.user import UserModel

async def verify_token(token: str):
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

def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request = kwargs['request']
        token = request.headers.get('Authorization', False)
        user = await verify_token(token)
        kwargs['request'].current_user = user
        return await func(*args, **kwargs)

    return wrapper
