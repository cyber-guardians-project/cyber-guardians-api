from fastapi import HTTPException, status
from api.dtos.requests.add_game_request_dto import AddGameRequestDto
from api.dtos.requests.update_game_request_dto import UpdateGameRequestDto
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

    async def update_game(self, game_id: str, game_data: UpdateGameRequestDto, user_id: str) -> None:
        existing_game = await game_repository.get_game(game_id, user_id)

        if not existing_game:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Game does not exists")

        update_data = game_data.model_dump(exclude_unset=True)

        updated = await game_repository.update_game(game_id, update_data)

        if not updated:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Error updating game")

    async def delete_game(self, game_id: str, user_id: str) -> None:
        existing_game = await game_repository.get_game(game_id, user_id)

        if not existing_game:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Game does not exists")

        deleted = await game_repository.delete_game(game_id)

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Error deleting game")
