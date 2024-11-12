from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from api.dtos.responses.standard_response_dto import StandardResponseDto


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        content=StandardResponseDto(
            status_code=exc.status_code,
            status="error",
            message=exc.detail,
            data=None
        ).model_dump(exclude_none=True),
        status_code=exc.status_code
    )
