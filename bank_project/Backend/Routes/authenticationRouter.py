from fastapi import APIRouter, HTTPException, Body
from Routes import input_validation
from auth.jwt_handler import signJWT
from Models.Users import Users
from Schemas.UserSchema import UserSchema
from Schemas.UserLoginSchema import UserLoginSchema

router = APIRouter()
validator = input_validation.Validator()
model_users = Users()


@router.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    model_users.add(user)
    return signJWT(user.user)

def check_user(user_details:UserLoginSchema):
    return model_users.validate(user_details)


@router.post("/user/login", tags=["user"])
def user_login(user:UserLoginSchema = Body()):
    if check_user(user):
        return signJWT(user.user)
    else:
        raise HTTPException(status_code = 404, detail="Bad Request: user does not exist")
