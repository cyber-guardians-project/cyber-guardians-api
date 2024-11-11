from typing import Optional
from api.dtos.requests.sign_up_request_dto import SignUpRequestDto
from api.dtos.responses.sign_up_response_dto import SignUpResponseDto
from api.models.user import User
from api.repositories.user_repository import UserRepository as user_repository
from api.utils.security import hash_password


class UserService:
    async def add_user(user_data: SignUpRequestDto) -> SignUpResponseDto:
        user_data.password = hash_password(user_data.password)
        created_user = await user_repository.add_user(user_data)

        return SignUpResponseDto(**created_user)

    async def get_user_by_email(user_email: str) -> Optional[User]:
        return await user_repository.get_user_by_email(user_email)
