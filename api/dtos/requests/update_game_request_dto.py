from typing import Optional
from pydantic import BaseModel


class UpdateGameRequestDto(BaseModel):
    score: Optional[int]
    character_variation: Optional[int]
    current_level: Optional[int]
    levels: Optional[dict]
