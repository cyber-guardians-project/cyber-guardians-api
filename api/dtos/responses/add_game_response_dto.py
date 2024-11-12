from typing import Optional
from pydantic import BaseModel


class AddGameResponseDto(BaseModel):
    id: str
    user_id: str
    score: int
    character_variation: int
    current_level: int
    levels: Optional[dict]
