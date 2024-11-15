from typing import Any

from bson import ObjectId
from api.config.database import database
from api.dtos.requests.add_game_request_dto import AddGameRequestDto
from api.dtos.responses.add_game_response_dto import AddGameResponseDto
from datetime import datetime, timezone

from api.dtos.responses.get_games_response_dto import GetGamesResponseDto


class GameRepository:
    async def get_games(self, user_id: str) -> GetGamesResponseDto:
        games_cursor = database.games.find({"user_id": user_id})
        games_list = await games_cursor.to_list(length=None)

        for game in games_list:
            game["id"] = str(game.pop("_id", None))

        return games_list

    async def add_game(self, game_data: AddGameRequestDto, user_id: int) -> AddGameResponseDto:
        game_document: dict[str, Any] = game_data.model_dump()
        game_document.update({
            "user_id": user_id,
            "created_at": datetime.now(timezone.utc)
        })

        created_game = await database.games.insert_one(game_document)
        game_document["id"] = str(created_game.inserted_id)

        return game_document
