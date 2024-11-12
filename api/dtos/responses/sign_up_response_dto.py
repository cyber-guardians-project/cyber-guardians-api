from pydantic import BaseModel, EmailStr
from datetime import datetime


class SignUpResponseDto(BaseModel):
    id: str
    user_name: str
    email: EmailStr
    birth_date: datetime
