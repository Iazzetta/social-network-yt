from typing import Annotated
from fastapi import APIRouter, Depends, Request
from src.api.dtos.posts import PostCreation, CommentCreation
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


@router.get('/{post_id}')
async def get_post(post_id: int, service: Annotated[PostService, Depends(PostService)]):
    post = await service.get_post(post_id)
    comments = await service.get_post_comments(post_id)
    return {
        "post": post,
        "comments": comments,
    }


@router.post('/{post_id}/like')
@login_required
async def like_post(
    request: Request,
    post_id: int, 
    service: Annotated[PostService, Depends(PostService)]
):
    response = await service.like_post(request.current_user.id, post_id)
    return {"like_post": response}

@router.post('/{post_id}/comment')
@login_required
async def comment_post(
    request: Request,
    post_id: int, 
    body: CommentCreation,
    service: Annotated[PostService, Depends(PostService)]
):
    response = await service.comment_post(request.current_user.id, post_id, body.message)
    return {"comment": response}


@router.get('/{post_id}/comments')
async def get_post_comments(
    post_id: int, 
    service: Annotated[PostService, Depends(PostService)]
):
    response = await service.get_post_comments(post_id)
    return {"comments": response}


@router.get('/{user_id}')
async def get_user_posts(
    user_id: int, 
    service: Annotated[PostService, Depends(PostService)]
):
    response = await service.get_user_posts(user_id)
    return {"posts": response}