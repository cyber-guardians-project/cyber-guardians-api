from api.utils.jwt_handler import create_access_token


class AuthService:
    def create_access_token(user_id: int):
        token_data = {"sub": user_id}
        access_token = create_access_token(data=token_data)

        return access_token
