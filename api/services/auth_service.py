from fastapi import HTTPException, status

from api.dtos.requests.sign_in_request_dto import SignInRequestDto
from api.models.user import User
from api.utils.jwt_handler import create_access_token
from api.services.user_service import UserService as user_service
from api.utils.security import verify_password


class AuthService:
    async def sign_in(user_credentials: SignInRequestDto):
        user: User = await user_service.get_user_by_email(user_credentials.email)

        if not user or not verify_password(user_credentials.password, user.password):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                                "Invalid email or password")

        return {'auth_token': create_access_token(user)}

    def _create_access_token(user: User):
        token_data = {"sub": user}
        access_token = create_access_token(data=token_data)

        return access_token
