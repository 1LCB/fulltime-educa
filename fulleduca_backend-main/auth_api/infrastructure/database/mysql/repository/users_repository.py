from app.entities.models.user_model import Users
from app.gateways.user_repository_gateway import UserRepositoryGateway
from infrastructure.database.mysql.settings.connection_handler import ConnectionHandler

class UserRepository(UserRepositoryGateway):
    @staticmethod
    def get_user_by_email(email: str) -> Users:
        with ConnectionHandler() as session:
            try:
                result = session.query(Users).filter(Users.email==email).first()
                return result
            except Exception as e:
                print(e)
                session.rollback()

    @staticmethod
    def get_user_by_id(id: int) -> Users:
        with ConnectionHandler() as session:
            try:
                result = session.query(Users).filter(Users.id==id).first()
                return result
            except Exception as e:
                print(e)
                session.rollback()

    @staticmethod
    def change_password(id: int, hashed_password: str) -> Users:
        with ConnectionHandler() as session:
            try:
                result = session.query(Users).filter(Users.id==id).first()
                result.password = hashed_password

                session.add(result)
                session.commit()
                session.refresh(result)

                return result
            except Exception as e:
                print(e)
                session.rollback()

