from typing import List, Optional
from django.contrib.auth.models import User
from ninja import ModelSchema
from ninja import Schema


class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = "__all__"
        exclude = ["password"]


class UserCreateSchema(Schema):
    username: str
    email: str
    password: str


class CustomResponseSchema(Schema):
    user_data: str = None
    message: str = None
    status_code: int = None
    success: bool = None
    error: bool = None


class UserListSchema(CustomResponseSchema):
    user_data: List[UserSchema]


class UserDetailSchema(CustomResponseSchema):
    user_data: Optional[UserSchema] = dict()
