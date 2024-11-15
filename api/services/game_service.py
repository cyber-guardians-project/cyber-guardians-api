from api.dtos.requests.add_game_request_dto import AddGameRequestDto
from api.dtos.responses.add_game_response_dto import AddGameResponseDto
from api.dtos.responses.get_games_response_dto import GetGamesResponseDto
from api.repositories.game_repository import GameRepository

game_repository = GameRepository()


class GameService:
    async def get_games(self, user_id: str) -> GetGamesResponseDto:
        return await game_repository.get_games(user_id)

    async def add_game(self, game_data: AddGameRequestDto, user_id: int) -> AddGameResponseDto:
        created_game = await game_repository.add_game(game_data, user_id)

        return AddGameResponseDto(**created_game)
