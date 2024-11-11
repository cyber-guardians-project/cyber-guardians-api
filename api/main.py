import uvicorn

from fastapi import FastAPI
from api.controllers.auth_controller import auth_router

api = FastAPI()

api.include_router(auth_router, prefix='/auth', tags=['Auth'])


if __name__ == '__main__':
    uvicorn.run(api, host="0.0.0.0", port=8000)