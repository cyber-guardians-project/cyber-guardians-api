from typing import Optional

from fastapi import HTTPException, status
from api.dtos.requests.sign_up_request_dto import SignUpRequestDto
from api.dtos.requests.update_user_request_dto import UpdateUserRequestDto
from api.dtos.responses.get_current_user_response_dto import GetCurrentUserResponseDto
from api.dtos.responses.sign_up_response_dto import SignUpResponseDto
from api.models.user import User
from api.repositories.user_repository import UserRepository
from api.utils.security import hash_password

user_repository = UserRepository()


class UserService:
    async def add_user(self, user_data: SignUpRequestDto) -> SignUpResponseDto:
        user_data.password = hash_password(user_data.password)
        existing_user = await user_repository.get_user_by_email(user_data.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="User with this email already exists.")

        created_user = await user_repository.add_user(user_data)

        return SignUpResponseDto(**created_user)

    async def get_user_by_email(self, user_email: str) -> Optional[User]:
        return await user_repository.get_user_by_email(user_email)

    async def update_user(self, user: GetCurrentUserResponseDto, user_data: UpdateUserRequestDto) -> User:
        existing_user = await user_repository.get_user_by_email(user['email'])

        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

        update_data = user_data.model_dump(exclude_unset=True)

        if "password" in update_data:
            update_data["password"] = hash_password(update_data["password"])

        if "email" in update_data:
            email_in_use = await self.get_user_by_email(update_data["email"])
            if email_in_use and email_in_use.id != user['id']:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Email is already in use by another user.",
                )

        updated = await user_repository.update_user(user['id'], update_data)

        if not updated:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error updating user",
            )

    async def delete_user_by_email(self, email: str):
        existing_user = await self.get_user_by_email(email)

        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

        deleted = await user_repository.delete_user_by_email(email)

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Error deleting user")
