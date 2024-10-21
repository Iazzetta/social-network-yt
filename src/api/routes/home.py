from fastapi import APIRouter, Request
from src.api.authentication import login_required

router = APIRouter(
    prefix="/me",
    tags=["me"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
@login_required
async def informations(request: Request):
    return {'user': request.current_user}

@router.get("/test")
@login_required
async def test_home(request: Request):
    return {'user': request.current_user}