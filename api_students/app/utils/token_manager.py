from infrastructure.config import get_environment_variables
from jwt.exceptions import PyJWTError
import jwt, time

env = get_environment_variables()


class TokenManager:
    @staticmethod
    def generate_token(info: dict) -> str:
        current_time = int(time.time())
        info["exp"] = current_time + env.ENV_TOKEN_EXP_SECONDS
        info["iat"] = current_time
        info["type"] = "access"

        token = jwt.encode(info, env.ENV_JWT_SECRET_KEY, env.ENV_JWT_ALGORITHM)
        return token

    @staticmethod
    def generate_new_refresh_token(info: dict):
        current_time = int(time.time())

        info["exp"] = current_time + (60 * 60 * 24 * env.ENV_REFRESH_TOKEN_EXP_DAYS)
        info["nbf"] = current_time + env.ENV_TOKEN_EXP_SECONDS
        info["iat"] = current_time
        info["type"] = "refresh"

        token = jwt.encode(info, env.ENV_JWT_SECRET_KEY, env.ENV_JWT_ALGORITHM)
        return token

    @staticmethod
    def is_valid(token: str) -> bool:
        try:
            jwt.decode(token, env.ENV_JWT_SECRET_KEY, algorithms=[env.ENV_JWT_ALGORITHM])
            return True
        except Exception as e:
            print("EXCEPTION: ", e)
            return False

    @staticmethod
    def decode(token) -> dict:
        return jwt.decode(token, env.ENV_JWT_SECRET_KEY, algorithms=[env.ENV_JWT_ALGORITHM])

    @staticmethod
    def refresh_token(token: str) -> str:
        decoded = jwt.decode(
            token, env.ENV_JWT_SECRET_KEY, algorithms=[env.ENV_JWT_ALGORITHM]
        )
        return TokenManager.generate_token({"user_id": decoded["user_id"]})
