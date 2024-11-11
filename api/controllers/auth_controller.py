from fastapi import APIRouter

from api.dtos.requests.sign_in_request_dto import SignInRequestDto
from api.dtos.responses.sign_up_response_dto import SignUpResponseDto
from api.dtos.responses.standard_response_dto import StandardResponseDto
from api.services.auth_service import AuthService as auth_service
from api.services.user_service import UserService as user_service
from api.dtos.requests.sign_up_request_dto import SignUpRequestDto
from api.utils.response_helper import create_standard_response

auth_router = APIRouter()


@auth_router.post('/sign-up')
async def sign_up(user_data: SignUpRequestDto) -> StandardResponseDto[SignUpResponseDto]:
    response = await user_service.add_user(user_data)

    return create_standard_response(status='success', message='User signed up successfully', data=response)


@auth_router.post('/sign-in')
async def sign_in(user_credentials: SignInRequestDto):
    response = await auth_service.sign_in(user_credentials)

    return create_standard_response(status='success', message='User signed in successfully', data=response)
