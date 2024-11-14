from fastapi import APIRouter, Depends, status

from api.dtos.responses.get_current_user_response_dto import GetCurrentUserResponseDto
from api.dtos.responses.standard_response_dto import StandardResponseDto
from api.utils.jwt_handler import get_session_user


users_router = APIRouter()


@users_router.get('/me')
def get_current_user(current_user: GetCurrentUserResponseDto
                     = Depends(get_session_user)) -> StandardResponseDto[GetCurrentUserResponseDto]:
    return StandardResponseDto(status_code=status.HTTP_200_OK,
                               status='success',
                               message='Current user',
                               data=current_user)
