from abc import ABC, abstractmethod
from app.entities.dto.user_dto import UserDTO


class UsersRepositoryGateway(ABC):
    @staticmethod
    @abstractmethod
    def create_new_user(user: UserDTO) -> int:
        pass

    @staticmethod
    @abstractmethod
    def delete_user_by_id(user_id: int) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def get_users_permissions_by_user_id(user_id: int) -> list[str]:
        pass