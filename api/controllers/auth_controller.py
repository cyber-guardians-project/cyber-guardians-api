from fastapi import APIRouter
from api.dtos.responses.sign_up_response_dto import SignUpResponseDto
from api.services.user_service import UserService
from api.dtos.requests.sign_up_request_dto import SignUpRequestDto

user_service = UserService
auth_router = APIRouter()


@auth_router.post("/sign-up")
async def sign_up(user_data: SignUpRequestDto) -> SignUpResponseDto:
    return await user_service.add_user(user_data)
