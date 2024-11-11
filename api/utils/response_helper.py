from typing import Any, Optional
from api.dtos.responses.standard_response_dto import StandardResponseDto


def create_standard_response(
    status: str,
    message: str = None,
    data: Optional[Any] = None
) -> StandardResponseDto:
    return StandardResponseDto(status=status, message=message, data=data)
