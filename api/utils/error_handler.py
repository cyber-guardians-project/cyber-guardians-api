from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from api.utils.response_helper import create_standard_response


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        content=create_standard_response(
            status="error",
            message=exc.detail,
            data=None
        ).model_dump(exclude_none=True),
        status_code=exc.status_code
    )
