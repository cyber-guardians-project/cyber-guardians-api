from typing import Any
from api.dtos.responses.standard_response_dto import StandardResponseDto


def create_standard_response(
    status: str,
    message: str = None,
    data: Any = None
) -> StandardResponseDto:
    return StandardResponseDto(status=status, message=message, data=data)
