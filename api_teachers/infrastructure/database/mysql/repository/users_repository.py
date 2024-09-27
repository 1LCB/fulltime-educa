from app.entities.models.db_models import User, Permission, GroupPermission
from app.entities.dto.user_dto import UserDTO
from infrastructure.database.mysql.settings.connection_handler import ConnectionHandler


class UsersRepository():
    @staticmethod
    def create_new_user(user: UserDTO) -> int:
        """
        Create a new user and return it's ID
        """
        with ConnectionHandler() as session:
            try:
                u = User(**user.model_dump())

                session.add(u)
                session.commit()
                session.refresh(u)
                
                return u.id
            except Exception as e:
                print("EXCEPTION", e)
                session.rollback()
                return None

    @staticmethod
    def get_users_permissions_by_user_id(user_id: int) -> list[str]:
        with ConnectionHandler() as session:
            try:
                user = session.query(User).filter_by(ID=user_id).first()
                if user is None:
                    return None

                group_id = user.group_id

                permissions = session.query(Permission).join(GroupPermission).\
                    filter(GroupPermission.group_id == group_id).all()

                return [permission.name for permission in permissions]
            except Exception as e:
                print("EXCEPTION TRYING TO GET USERS PERMISSION: ", e)
                session.rollback()

    @staticmethod
    def delete_user_by_id(user_id: int) -> bool:
        with ConnectionHandler() as session:
            try:
                affected_rows = session.query(User).filter(User.id==user_id).delete()
                return affected_rows > 0
            except Exception as e:
                print("EXCEPTION", e)
                session.rollback()
                return False
