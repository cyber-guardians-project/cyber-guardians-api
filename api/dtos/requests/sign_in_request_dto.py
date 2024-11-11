from pydantic import BaseModel, EmailStr


class SignUpRequestDto(BaseModel):
    email: EmailStr
    password: str
