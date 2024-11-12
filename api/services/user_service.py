from typing import Optional

from fastapi import HTTPException
from api.dtos.requests.sign_up_request_dto import SignUpRequestDto
from api.dtos.responses.sign_up_response_dto import SignUpResponseDto
from api.models.user import User
from api.repositories.user_repository import UserRepository as user_repository
from api.utils.security import hash_password


class UserService:
    async def add_user(user_data: SignUpRequestDto) -> SignUpResponseDto:
        user_data.password = hash_password(user_data.password)
        existing_user = await user_repository.get_user_by_email(user_data.email)

        if existing_user:
            raise HTTPException(
                status_code=409, detail="User with this email already exists.")

        created_user = await user_repository.add_user(user_data)

        return SignUpResponseDto(**created_user)

    async def get_user_by_email(user_email: str) -> Optional[User]:
        return await user_repository.get_user_by_email(user_email)