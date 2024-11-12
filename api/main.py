from fastapi import FastAPI
from fastapi import HTTPException

from api.controllers.auth_controller import auth_router
from api.controllers.users_controller import users_router

from api.config.settings import settings
from api.utils.error_handler import http_exception_handler


api = FastAPI(title=settings.app_name)

api.add_exception_handler(HTTPException, http_exception_handler)

api.include_router(auth_router, prefix='/auth', tags=['Auth'])
api.include_router(users_router, prefix='/users', tags=['Users'])
