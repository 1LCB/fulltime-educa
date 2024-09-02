from abc import ABC, abstractmethod
from app.entities.dto.student_dto import StudentReadDTO, StudentUpdateDTO
from app.entities.dto.student_dto import StudentInsertInDatabase


class StudentRepositoryGateway(ABC):
    @staticmethod
    @abstractmethod
    def get_all_students() -> list[StudentReadDTO]:
        pass

    @staticmethod
    @abstractmethod
    def insert_student(student: StudentInsertInDatabase) -> int:
        pass

    @staticmethod
    @abstractmethod
    def get_student_by_id(id: int):
        pass

    @staticmethod
    @abstractmethod
    def delete_student_by_id(student_id: int) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def update_student(student: StudentUpdateDTO) -> dict:
        pass
