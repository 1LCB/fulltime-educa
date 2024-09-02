from abc import ABC, abstractmethod
from app.entities.models.user_model import Users


class UserRepositoryGateway(ABC):
    @staticmethod
    @abstractmethod
    def get_user_by_email(email: str) -> Users:
        pass

    
    @staticmethod
    @abstractmethod
    def get_user_by_id(id: int) -> Users:
        pass


    @staticmethod
    @abstractmethod
    def change_password(id: int, hashed_password: str) -> Users:
        pass