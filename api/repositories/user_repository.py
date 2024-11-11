from typing import Any, Optional

from api.config.database import database
from api.dtos.requests.sign_up_request_dto import SignUpRequestDto
from api.dtos.responses.sign_up_response_dto import SignUpResponseDto
from api.models.user import User


class UserRepository:
    async def add_user(user_data: SignUpRequestDto) -> SignUpResponseDto:
        user_document: dict[str, Any] = user_data.model_dump()
        created_user: User = await database.users.insert_one(user_document)
        user_document["id"] = str(created_user.inserted_id)

        return user_document

    async def get_user_by_email(user_email: str) -> Optional[User]:
        user_document = await database.users.find_one({"email": user_email})

        if user_document:
            user_document["_id"] = str(user_document["_id"])
            return User(**user_document)

        return None
