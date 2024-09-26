from pydantic_settings import BaseSettings


class EnvironmentVariables(BaseSettings):
    ENV_MYSQL_USER: str
    ENV_MYSQL_PASS: str
    ENV_MYSQL_BASE: str
    ENV_MYSQL_HOST: str
    ENV_MYSQL_PORT: int
    ENV_TOKEN_EXP_SECONDS: int
    ENV_REFRESH_TOKEN_EXP_DAYS: int
    ENV_JWT_SECRET_KEY: str
    ENV_JWT_ALGORITHM: str

    class Config:
        env_file = ".env"


def get_environment_variables() -> EnvironmentVariables:
    return EnvironmentVariables()
