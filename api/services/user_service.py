from api.dtos.requests.sign_up_request_dto import SignUpRequestDto
from api.dtos.responses.sign_up_response_dto import SignUpResponseDto
from api.repositories.user_repository import UserRepository

user_repository = UserRepository


class UserService:
    async def add_user(user_data: SignUpRequestDto) -> SignUpResponseDto:
        created_user = await user_repository.add_user(user_data)

        return SignUpResponseDto(**created_user)
