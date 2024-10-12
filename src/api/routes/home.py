from fastapi import APIRouter
from src.datalayer.models.user import UserModel
from typing import Annotated
from fastapi import Depends
from src.api.authentication import verify_token

router = APIRouter(
    prefix="/me",
    tags=["me"],
    responses={404: {"description": "Not found"}},
)

# meu token: 6mkMH-YjLU1SbYjZ5WBeE9pkNQ8

@router.post("/")
async def informations(current_user: Annotated[UserModel, Depends(verify_token)]):
    return {'user': current_user}