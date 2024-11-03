from src.datalayer.models.user import UserModel
from src.datalayer.models.post import PostModel, PostLikeModel, PostCommentModel
from tortoise.exceptions import DoesNotExist
from src.api.exceptions.post import post_notfound

class PostService:

    def __init__(self):
        pass

    
    async def create_post(self, user: UserModel, message: str):
        new_post = await PostModel.create(
            user = user,
            message = message,
        )
        return new_post

    async def get_post(self, post_id: int):
        try:
            return await PostModel.get(id=post_id)
        except DoesNotExist as e:
            raise post_notfound()

    async def like_post(self, user_id: int, post_id: int):
        post = await PostModel.get(id = post_id)

        try:
            post_like = await PostLikeModel.get(
                user_id = user_id, 
                post_id = post_id
            )
            await post_like.delete()
            post.likes_count -= 1

        except DoesNotExist as e:
            await PostLikeModel.create(
                user_id = user_id,
                post_id = post_id,
            )
            post.likes_count += 1

        finally:
            await post.save()

        return post.likes_count

    async def comment_post(self, user_id: int, post_id: int, message: str):

        post = await PostModel.get(id = post_id)

        comment = await PostCommentModel.create(
            user_id = user_id,
            post_id = post_id,
            message = message
        )

        post.comments_count += 1
        await post.save()

        return comment

    async def get_post_comments(self, post_id: int):
        return await PostCommentModel.filter(post_id = post_id).order_by('-created_at')

    async def get_all_posts(self):
        return await PostModel.all().order_by('-created_at')
        
    async def get_user_posts(self, user_id: int):
        return await PostModel.filter(user_id=user_id)