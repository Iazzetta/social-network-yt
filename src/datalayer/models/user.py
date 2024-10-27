import secrets
from tortoise.models import Model
from tortoise import fields
from src.datalayer.models.base import ModelBase


def generate_token():
    return secrets.token_urlsafe(50)

class UserModel(ModelBase):
    name = fields.CharField(max_length=240)
    email = fields.CharField(max_length=240, unique=True)
    password = fields.TextField()
    token = fields.TextField(default=generate_token)
