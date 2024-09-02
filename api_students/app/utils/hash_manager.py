from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashManager:
    @staticmethod
    def verify_hash(raw_pwd: str, hashed_pwd: str) -> bool:
        return pwd_ctx.verify(raw_pwd, hashed_pwd)

    @staticmethod
    def hash_password(raw_pwd: str) -> str:
        return pwd_ctx.hash(raw_pwd, salt_size=22, rounds=15)
