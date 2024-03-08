from ninja import Router
from django.contrib.auth.models import User
# Create your views here.
from .schema import UserListSchema, UserDetailSchema, UserSchema, UserCreateSchema
from django.http import HttpResponse, JsonResponse
router = Router()


@router.get("/users", response=UserListSchema)
def get_users_list(request):
    user_data = list(User.objects.all())
    response_data = {"user_data": user_data, "message": "user data get successfully", "status_code": 200}
    return response_data


@router.get("/users/{user_id}/", response=UserDetailSchema)
def get_user_detail(request, user_id: int):
    user_data = User.objects.filter(id=user_id).first()

    if user_data:
        response_data = {
            "user_data": user_data,
            "message": "Specific user data retrieved successfully",
            "status_code": 200
        }
        return response_data
    else:
        return JsonResponse({"message": f"User with id {user_id} does not exist", "status_code": 404}, status=404)


@router.post("/signup", response=UserSchema)
def signup(request, payload: UserCreateSchema):
    # Assuming UserSchema corresponds to your User model
    new_user = User.objects.create_user(**payload.dict())
    return new_user
