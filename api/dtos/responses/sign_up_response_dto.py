from pydantic import BaseModel, EmailStr
from datetime import datetime


class SignUpResponseDto(BaseModel):
    id: str
    user_name: str
    email: EmailStr
    password: str
    birth_date: datetime
