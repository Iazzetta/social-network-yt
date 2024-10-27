from typing import Annotated
from fastapi import APIRouter, Depends
from src.api.dtos.users import UserRegistration, UserLogin
from src.services.user import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/register")
async def register(body: UserRegistration, service: Annotated[UserService, Depends(UserService)]):

    response = await service.register(
        name=body.name, 
        email=body.email, 
        password=body.password
    )

    return {'token': response}

@router.post("/login")
async def login(
    body: UserLogin, 
    service: Annotated[UserService, Depends(UserService)]
):

    response = await service.login(
        email=body.email,
        password=body.password
    )

    return {'token': response}

@router.get('/all-users')
async def get_all_users(service: Annotated[UserService, Depends(UserService)]):
    return await service.get_all_users()


@router.get('/get-mini-user/{user_id}')
async def get_mini_user(user_id: int, service: Annotated[UserService, Depends(UserService)]):
    return await service.get_mini_user(user_id)