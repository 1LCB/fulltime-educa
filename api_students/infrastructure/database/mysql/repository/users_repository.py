from app.entities.models.db_models import Users
from app.entities.dto.user_dto import UserDTO
from infrastructure.database.mysql.settings.connection_handler import ConnectionHandler


class UsersRepository():
    @staticmethod
    def create_new_user(user: UserDTO) -> int:
        """
        Create a new user and return it's id
        """
        with ConnectionHandler() as session:
            try:
                dumped = user.model_dump()
                u = Users(
                    name=dumped["name"],
                    email=dumped["email"],
                    password=dumped["password"],
                    group_id=dumped["group_id"],
                    image_path=dumped["image_path"]
                )

                session.add(u)
                session.commit()
                session.refresh(u)

                return u.id
            except Exception as e:
                print(e)
                session.rollback()
        return None
            
    @staticmethod
    def delete_user_by_id(user_id: int) -> bool:
        with ConnectionHandler() as session:
            try:
                affected_rows = session.query(Users).filter(Users.id==user_id).delete()
                return affected_rows > 0
            except Exception as e:
                print("EXCEPTION", e)
                session.rollback()
        return False
