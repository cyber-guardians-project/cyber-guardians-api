from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer

from api.dtos.responses.get_current_user_response_dto import GetCurrentUserResponseDto
from api.dtos.responses.standard_response_dto import StandardResponseDto
from api.utils.jwt_handler import verify_access_token


users_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@users_router.get('/me')
def get_current_user(token: str = Depends(oauth2_scheme)) -> StandardResponseDto[GetCurrentUserResponseDto]:
    payload = verify_access_token(token)
    user = payload

    return StandardResponseDto(status_code=status.HTTP_200_OK, status='success',
                               message='Current user', data=user)
