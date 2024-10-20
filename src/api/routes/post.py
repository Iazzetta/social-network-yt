from typing import Annotated
from fastapi import APIRouter, Depends, Request
from src.api.dtos.posts import PostCreation
from src.services.post import PostService
from src.api.authentication import login_required

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create")
@login_required
async def create_post(
    body: PostCreation, 
    service: Annotated[PostService, Depends(PostService)],
    request: Request,
):

    response = await service.create_post(
        user=request.current_user, 
        message=body.message
    )

    return {'post': response}

@router.get('/all-posts')
async def get_posts(service: Annotated[PostService, Depends(PostService)]):
    response = await service.get_all_posts()
    return {"posts": response}


@router.post('/{post_id}/like')
@login_required
async def like_post(
    request: Request,
    post_id: int, 
    service: Annotated[PostService, Depends(PostService)]
):
    response = await service.like_post(request.current_user.id, post_id)
    return {"like_post": response}

@router.get('/{user_id}')
async def get_user_posts(
    user_id: int, 
    service: Annotated[PostService, Depends(PostService)]
):
    response = await service.get_user_posts(user_id)
    return {"posts": response}