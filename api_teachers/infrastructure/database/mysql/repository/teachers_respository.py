from app.entities.models.db_models import Teachers, Users
from app.entities.dto.teacher_dto import TeacherInsertInDatabaseDTO, TeacherUpdateDTO
from app.gateways.teacher_repository_gateway import TeacherRepositoryGateway
from infrastructure.database.mysql.settings.connection_handler import ConnectionHandler
from infrastructure.database.mysql.repository.users_repository import UsersRepository, Users

class TeacherRepository(TeacherRepositoryGateway):
    @staticmethod
    def get_all_teachers() -> list[dict]:
        with ConnectionHandler() as session:
            try:
                teachers = session.query(
                    Teachers.cpf,
                    Teachers.id,
                    Teachers.user_id,
                    Users.email,
                    Users.name,
                    Users.image_path
                ).join(
                    Users,
                    Users.id == Teachers.user_id
                ).all()
                return teachers
            except Exception as e:
                print("EXCEPTION", e)
                session.rollback()

    @staticmethod
    def insert_teacher(teacher: TeacherInsertInDatabaseDTO) -> int:
        with ConnectionHandler() as session:
            try:
                p = Teachers(cpf=teacher.cpf, user_id=teacher.user_id)

                session.add(p)
                session.commit()
                session.refresh(p)

                return p.id
            except Exception as e:
                print("EXCEPTION", e)
                session.rollback()
        return None

    @staticmethod
    def get_teacher_by_id(id: int) -> Teachers:
        with ConnectionHandler() as session:
            try:
                r = session.query(
                    Teachers.cpf,
                    Teachers.id,
                    Teachers.user_id,
                    Users.email,
                    Users.name,
                    Users.image_path
                ).join(
                    Users,
                    Users.id == Teachers.user_id
                ).filter(
                    Teachers.id == id
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
                teacher = session.query(Teachers).filter(Teachers.id==teacher_id).first()
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
                t = session.query(Teachers).filter(Teachers.id==teacher.id).first()
                t.cpf = teacher.cpf
                
                u = session.query(Users).filter(
                    Users.id==t.user_id
                ).first()

                u.name = teacher.name
                u.email = teacher.email

                session.commit()
                return t.id
            except Exception as e:
                print("EXCEPTION UPDATE", e)
                session.rollback()
        return None