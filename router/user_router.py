from fastapi import APIRouter

user_r = APIRouter(tags=["user"], prefix="/user")


@user_r.get("/")
async def user():
    return {
        "code": 200,
        "msg": "hello user"
    }
