from pydantic import BaseModel, EmailStr
from datetime import datetime


class SignUpRequestDto(BaseModel):
    user_name: str
    email: EmailStr
    password: str
    birth_date: datetime
