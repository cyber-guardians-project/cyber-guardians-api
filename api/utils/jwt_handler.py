import jwt
from api.config.settings import settings


def create_access_token(user_id: int) -> str:
    to_encode = user_id.copy()

    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.jwt_algorithm)

    return encoded_jwt


def verify_access_token(token: str) -> int:
    try:
        payload = jwt.decode(token, settings.secret_key,
                             algorithms=[settings.jwt_algorithm])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
