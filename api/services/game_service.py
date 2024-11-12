from api.dtos.requests.add_game_request_dto import AddGameRequestDto
from api.dtos.responses.add_game_response_dto import AddGameResponseDto
from api.repositories.game_repository import GameRepository as game_repository


class GameService:
    async def add_game(game_data: AddGameRequestDto, user_id: int) -> AddGameResponseDto:
        created_game = await game_repository.add_game(game_data, user_id)

        return AddGameResponseDto(**created_game)
