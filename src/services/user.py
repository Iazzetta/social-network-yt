from src.datalayer.models.user import UserModel
from src.api.exceptions.user import (
    login_wrong_exception, 
    email_already_exists
)

class UserService:

    def __init__(self):
        pass

    async def register(self, name: str, email: str, password: str):

        email_exists = await UserModel.filter(email=email)
        if email_exists:
            raise email_already_exists()

        user = await UserModel.create(
            name = name,
            email = email,
            password = password
        )

        return user.token

    async def login(self, email: str, password: str):
        user = None
        try:
            user = await UserModel.get(email=email)
        except Exception as e:
            raise login_wrong_exception()

        if user.password != password:
            raise login_wrong_exception()

        return user.token

    async def get_all_users(self):
        return await UserModel.all().values('id', 'name')

    async def get_mini_user(self, user_id: int):
        return await UserModel.get(id=user_id).values('id', 'name')
