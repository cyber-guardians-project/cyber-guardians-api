from api.dtos.requests.sign_up_request_dto import SignUpRequestDto
from api.dtos.responses.sign_up_response_dto import SignUpResponseDto
from api.repositories.user_repository import UserRepository as user_repository
from api.services.auth_service import AuthService as auth_service


class UserService:
    async def add_user(user_data: SignUpRequestDto) -> SignUpResponseDto:
        created_user = await user_repository.add_user(user_data)

        return SignUpResponseDto(**created_user)
