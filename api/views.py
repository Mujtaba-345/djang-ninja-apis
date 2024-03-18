from ninja import Router
from django.contrib.auth.models import User
# Create your views here.
from .schema import UserListSchema, UserDetailSchema, UserCreateSchema, UserSignupSchema
from django.http import JsonResponse

router = Router()


@router.get("/users", response=UserListSchema)
def get_users_list(request):
    """
    get list of users
    """
    user_data = User.objects.all()
    response_data = {"user_data": user_data, "message": "user data get successfully", "status_code": 200,
                     "success": "true"}
    return response_data


@router.get("/users/{user_id}/", response=UserDetailSchema)
def get_user_detail(request, user_id: int):
    """
    get single user details
    """
    user_data = User.objects.filter(id=user_id).first()
    if user_data:
        response_data = {
            "user_data": user_data,
            "message": "Specific user data retrieved successfully",
            "status_code": 200,
            "success": "true",
        }
        return response_data
    else:
        return JsonResponse({"message": f"User with id {user_id} does not exist", "status_code": 404, "error": "true"},
                            status=404)


@router.post("/signup", response=UserSignupSchema)
def signup(request, payload: UserCreateSchema):
    """
    User Signup functionality
    """
    try:
        new_user = User.objects.create_user(**payload.dict())
        response_data = {
            "user_data": new_user,
            "message": "user created successfully",
            "status_code": 200,
            "success": "true"
        }
        return response_data
    except Exception:
        return JsonResponse(
            {"message": f"User with this username {payload.username} is already exist", "status_code": 400,
             "error": "true"},
            status=400)
