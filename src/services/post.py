from src.datalayer.models.user import UserModel
from src.datalayer.models.post import PostModel

class PostService:

    def __init__(self):
        pass

    
    async def create_post(self, user: UserModel, message: str):
        new_post = await PostModel.create(
            user = user,
            message = message,
        )
        return new_post

    async def get_all_posts(self):
        return await PostModel.all()
        
    async def get_user_posts(self, user_id: int):
        return await PostModel.filter(user_id=user_id)