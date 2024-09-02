from app.entities.models.db_models import Students, Users
from app.entities.dto.student_dto import StudentInsertInDatabase, StudentReadDTO, StudentUpdateDTO
from app.gateways.students_repository_gateway import StudentRepositoryGateway
from infrastructure.database.mysql.settings.connection_handler import ConnectionHandler

class StudentRepository(StudentRepositoryGateway):
    @staticmethod
    def get_all_students() -> list:
        with ConnectionHandler() as session:
            try:
                students = session.query(
                    Students.id,
                    Students.user_id,
                    Students.date_of_birth,
                    Students.gender,
                    Students.ethnicity,
                    Students.birth_city,
                    Students.id_card,
                    Students.cpf,
                    Students.phone,
                    Students.address,
                    Students.residential_complement,
                    Students.father_name,
                    Students.mother_name,
                    Students.school_attended,
                    Students.current_school,
                    Students.shift,
                    Students.sector_id,
                    Students.admission_date,
                    Students.completion_date,
                    Students.course_status,
                    Students.total_classes,
                    Students.attendances,
                    Students.absences,
                    Users.name,
                    Users.email,
                    Users.image_path,
                ).join(
                    Users,
                    Students.user_id == Users.id,
                ).all()
                return students
            except Exception as e:
                print("exception: ", e)
                session.rollback()
        return []

    @staticmethod
    def insert_student(student: StudentInsertInDatabase) -> int:
        with ConnectionHandler() as session:
            try:
                p = Students()

                dumped = student.model_dump()
                for k, v in dumped.items():
                    setattr(p, k, v)

                session.add(p)
                session.commit()
                session.refresh(p)

                return p.id
            except Exception as e:
                print("EXCEPTION", e)
                session.rollback()
        return None

    @staticmethod
    def get_student_by_id(id: int):
        with ConnectionHandler() as session:
            try:
                r = session.query(
                    Students.id,
                    Students.user_id,
                    Students.date_of_birth,
                    Students.gender,
                    Students.ethnicity,
                    Students.birth_city,
                    Students.id_card,
                    Students.cpf,
                    Students.phone,
                    Students.address,
                    Students.residential_complement,
                    Students.father_name,
                    Students.mother_name,
                    Students.school_attended,
                    Students.current_school,
                    Students.shift,
                    Students.sector_id,
                    Students.admission_date,
                    Students.completion_date,
                    Students.course_status,
                    Students.total_classes,
                    Students.attendances,
                    Students.absences,
                    Users.name,
                    Users.email,
                    Users.image_path,
                ).join(
                    Users,
                    Students.user_id == Users.id,
                ).filter(
                    Students.id == id
                ).first()

                return r
            except Exception as e:
                print("EXCEPTION", e)
                session.rollback()
        return None

    @staticmethod
    def delete_student_by_id(student_id: int) -> bool:
        with ConnectionHandler() as session:
            try:
                student = session.query(Students).filter(Students.id==student_id).first()
                session.delete(student)
                session.commit()
                return student
            except Exception as e:
                print("EXCEPTION", e)
                session.rollback()
        return None

    @staticmethod
    def update_student(student: StudentUpdateDTO) -> dict:
        with ConnectionHandler() as session:
            try:
                t = session.query(Students).filter(Students.id==student.id).first()
                dumped = student.model_dump(exclude_none=True)
            
                for k, v in dumped.items():
                    setattr(t, k, v)
                
                session.commit()
                return {"id": t.id}
            except Exception as e:
                print("EXCEPTION UPDATE", e)
                session.rollback()
        return None