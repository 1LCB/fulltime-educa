from app.gateways.teacher_repository_gateway import TeacherRepositoryGateway
from app.gateways.users_repository_gateway import UsersRepositoryGateway
from app.gateways.email_sender_gateway import EmailSenderGateway
from app.entities.http.http_response import HTTPResponse
from app.entities.dto.teacher_dto import TeacherPostRequest, TeacherUpdateDTO, TeacherInsertInDatabaseDTO, TeacherReadDTO
from app.entities.dto.user_dto import UserDTO
from app.utils.hash_manager import HashManager
from http import HTTPStatus
from functools import wraps
import string, random, base64, uuid

# def has_permission(permission_name: str):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(self, *args, user_id=None, **kwargs):
#             permissions = self.users_repository.get_users_permissions_by_user_id(user_id)
#             if not permission_name in permissions:
#                 return HTTPResponse(
#                     status_code=HTTPStatus.FORBIDDEN,
#                     content={"detail": "Acesso proibido"}
#                 )
#             return func(self, *args, **kwargs)
#         return wrapper
#     return decorator

class TeachersUseCase:
    def __init__(
        self,
        teachers_repository: TeacherRepositoryGateway,
        users_repository: UsersRepositoryGateway,
        email_sender: EmailSenderGateway
    ) -> None:
        self.teachers_repository = teachers_repository
        self.users_repository = users_repository
        self.email_sender = email_sender

    def get_all_teachers(self, user_id: int) -> HTTPResponse:
        teachers = self.teachers_repository.get_all_teachers()

        response = [
            TeacherReadDTO(
                id=t.id,
                name=t.name,
                cpf=t.cpf,
                email=t.email,
                image_path=t.image_path,
                user_id=t.user_id
            ).model_dump() for t in teachers
        ]

        return HTTPResponse(
            status_code=HTTPStatus.OK,
            content=response,
        )
    
    def get_teacher_by_id(self, teacher_id: int, user_id:int) -> HTTPResponse:
        teacher = self.teachers_repository.get_teacher_by_id(teacher_id)
        if teacher is None:
            return HTTPResponse(
                status_code=HTTPStatus.NOT_FOUND,
                content={"detail": "teacher has not been found!"}
            )

        teacher_response = TeacherReadDTO(
            id=teacher.id,
            name=teacher.name,
            cpf=teacher.cpf,
            email=teacher.email,
            image_path=teacher.image_path,
            user_id=teacher.user_id
        ).model_dump()

        return HTTPResponse(
            status_code=HTTPStatus.OK,
            content=teacher_response
        )

    def create_new_teacher(self, teacher_create: TeacherPostRequest, user_id: int):
        image_filename = self.save_photo(teacher_create.image)
        password = self.generate_random_password(10)
        print("PASSWORD: ", password)

        hashed_psasword = HashManager.hash_password(password)
        user_id = self.users_repository.create_new_user(
            user=UserDTO(
                **teacher_create.model_dump(), 
                password=hashed_psasword, 
                image_path=image_filename
            )
        )

        t = TeacherInsertInDatabaseDTO(**teacher_create.model_dump(), user_id=user_id)
        teacher = self.teachers_repository.insert_teacher(t)
        if teacher is None:
            return HTTPResponse(
                content={"detail", "an error ocurred during the insertion process"},
                status_code=HTTPStatus.BAD_REQUEST,
            )
        
        self.email_sender.send_email(t.name, t.email, password)

        teacher_db = self.teachers_repository.get_teacher_by_id(teacher)
        response = TeacherReadDTO(
            id=teacher_db.id,
            name=teacher_db.name,
            cpf=teacher_db.cpf,
            email=teacher_db.email,
            image_path=teacher_db.image_path,
            user_id=teacher_db.user_id
        ).model_dump()

        return HTTPResponse(
            status_code=HTTPStatus.OK,
            content=response
        )

    def delete_teacher(self, teacher_id: int, user_id: int):
        deleted = self.teachers_repository.delete_teacher_by_id(teacher_id)
        if not deleted:
            return HTTPResponse(status_code=HTTPStatus.BAD_REQUEST, content={
                "detail": f"something went wrong when trying to delete teacher {teacher_id}"
            })
        return HTTPResponse(
            status_code=HTTPStatus.OK,
            content={
                "info": f"teacher {teacher_id} deleted successfully"
            }
        )
    
    def update_teacher(self, teacher_update: TeacherUpdateDTO, user_id: int):
        resp = self.teachers_repository.update_teacher(teacher_update)
        if resp is None:
            return HTTPResponse(
                status_code=HTTPStatus.BAD_REQUEST,
                content={"detail": "something went wrong when trying to update user"}
            )
        response = self.teachers_repository.get_teacher_by_id(resp)

        teacher_response = TeacherReadDTO(
            id=response.id,
            name=response.name,
            cpf=response.cpf,
            email=response.email,
            image_path=response.image_path,
            user_id=response.user_id
        ).model_dump()

        return HTTPResponse(
            status_code=HTTPStatus.OK,
            content=teacher_response
        )

    def generate_random_password(self, size: int) -> str:
        return "".join(random.sample(list(string.ascii_lowercase + string.ascii_uppercase + string.digits), size))
    
    def save_photo(self, photo_base64: str) -> str:
        try:
            filename = f"{uuid.uuid4()}.jpg"
            with open(f"app/uploads/{filename}", "wb") as file:
                file.write(base64.b64decode(photo_base64))
            return filename
        except Exception as e:
            print("Exception when trying to decode base64:", e)
        return "unknown.png"