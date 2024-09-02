from abc import ABC, abstractmethod
from app.entities.dto.teacher_dto import TeacherUpdateDTO
from app.entities.dto.teacher_dto import TeacherInsertInDatabaseDTO
from app.entities.models.db_models import Teachers

class TeacherRepositoryGateway(ABC):
    @staticmethod
    @abstractmethod
    def get_all_teachers() -> list:
        pass

    @staticmethod
    @abstractmethod
    def insert_teacher(teacher: TeacherInsertInDatabaseDTO) -> int:
        pass

    @staticmethod
    @abstractmethod
    def get_teacher_by_id(id: int) -> Teachers:
        pass

    @staticmethod
    @abstractmethod
    def delete_teacher_by_id(teacher_id: int) -> int:
        pass

    @staticmethod
    @abstractmethod
    def update_teacher(teacher: TeacherUpdateDTO) -> int:
        pass
