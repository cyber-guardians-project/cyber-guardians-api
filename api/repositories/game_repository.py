from typing import Any
from api.config.database import database
from api.dtos.requests.add_game_request_dto import AddGameRequestDto
from api.dtos.responses.add_game_response_dto import AddGameResponseDto
from api.models.game import Game


class GameRepository:
    async def add_game(game_data: AddGameRequestDto, user_id: int) -> AddGameResponseDto:
        game_document: dict[str, Any] = game_data.model_dump()
        game_document['user_id'] = user_id

        created_game: Game = await database.games.insert_one(game_document)
        game_document["id"] = str(created_game.inserted_id)

        return game_document
