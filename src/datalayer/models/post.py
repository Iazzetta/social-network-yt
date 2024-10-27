import secrets
from tortoise.models import Model
from tortoise import fields
from src.datalayer.models.base import ModelBase

class PostModel(ModelBase):
    user = fields.ForeignKeyField('models.UserModel', related_name='posts')
    message = fields.TextField()
    likes_count = fields.IntField(default=0)
    comments_count = fields.IntField(default=0)

class PostLikeModel(ModelBase):
    user = fields.ForeignKeyField('models.UserModel', related_name='user_likes')
    post = fields.ForeignKeyField('models.PostModel', related_name='post_likes')


class PostCommentModel(ModelBase):
    user = fields.ForeignKeyField('models.UserModel', related_name='user_comments')
    post = fields.ForeignKeyField('models.PostModel', related_name='post_comments')
    message = fields.TextField()