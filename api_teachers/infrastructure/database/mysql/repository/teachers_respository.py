from app.entities.models.db_models import Teacher, User
from app.entities.dto.teacher_dto import TeacherInsertInDatabaseDTO, TeacherUpdateDTO
from app.gateways.teacher_repository_gateway import TeacherRepositoryGateway
from infrastructure.database.mysql.settings.connection_handler import ConnectionHandler
from infrastructure.database.mysql.repository.users_repository import UsersRepository

class TeacherRepository(TeacherRepositoryGateway):
    @staticmethod
    def get_all_teachers() -> list[Teacher | User]:
        with ConnectionHandler() as session:
            try:
                teachers = session.query(
                    Teacher.id,
                    Teacher.address,
                    Teacher.phone,
                    Teacher.user_id,
                    User.email,
                    User.name,
                    User.image_path
                ).join(
                    User,
                    User.id == Teacher.user_id
                ).all()
                return teachers
            except Exception as e:
                print("EXCEPTION", e)
                session.rollback()

    @staticmethod
    def insert_teacher(teacher: TeacherInsertInDatabaseDTO) -> int:
        with ConnectionHandler() as session:
            try:
                p = Teacher(address=teacher.address,phone=teacher.phone, user_id=teacher.user_id)

                session.add(p)
                session.commit()
                session.refresh(p)

                return p.id
            except Exception as e:
                print("EXCEPTION", e)
                session.rollback()
        return None

    @staticmethod
    def get_teacher_by_id(id: int) -> Teacher:
        with ConnectionHandler() as session:
            try:
                r = session.query(
                    Teacher.id,
                    Teacher.user_id,
                    Teacher.phone,
                    Teacher.address,
                    User.email,
                    User.name,
                    User.image_path
                ).join(
                    User,
                    User.id == Teacher.user_id
                ).filter(
                    Teacher.id == id
                ).first()
                return r
            except Exception as e:
                print("EXCEPTION", e)
                session.rollback()
        return None

    @staticmethod
    def delete_teacher_by_id(teacher_id: int) -> bool:
        with ConnectionHandler() as session:
            try:
                teacher = session.query(Teacher).filter(Teacher.id==teacher_id).first()
                session.delete(teacher)
                session.commit()
                return True
            except Exception as e:
                print("EXCEPTION", e)
                session.rollback()
        return False
            


    @staticmethod
    def update_teacher(teacher: TeacherUpdateDTO) -> int:
        with ConnectionHandler() as session:
            try:
                t = session.query(Teacher).filter(Teacher.id==teacher.id).first()
                
                t.address = teacher.address
                t.phone = teacher.phone

                u = session.query(User).filter(
                    User.id==t.user_id
                ).first()

                u.name = teacher.name
                u.email = teacher.email

                session.commit()
                return t.id
            except Exception as e:
                print("EXCEPTION UPDATE", e)
                session.rollback()
        return None