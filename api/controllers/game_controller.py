from fastapi import APIRouter, Depends, status


from api.dtos.requests.add_game_request_dto import AddGameRequestDto
from api.dtos.responses.add_game_response_dto import AddGameResponseDto
from api.dtos.responses.get_current_user_response_dto import GetCurrentUserResponseDto
from api.dtos.responses.standard_response_dto import StandardResponseDto
from api.services.game_service import GameService as game_service
from api.utils.jwt_handler import get_session_user


games_router = APIRouter()


@games_router.post('')
async def add_game(game_data: AddGameRequestDto,
                   current_user: GetCurrentUserResponseDto =
                   Depends(get_session_user)) -> StandardResponseDto[AddGameResponseDto]:
    response = await game_service.add_game(game_data, current_user['id'])

    return StandardResponseDto(status_code=status.HTTP_200_OK, status='success',
                               message='Game created', data=response)
