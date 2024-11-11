from fastapi import APIRouter


auth_router = APIRouter()

@auth_router.get("/sign-in")
async def sign_in():
    pass
    