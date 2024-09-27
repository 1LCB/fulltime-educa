from fastapi import APIRouter, status, Depends, Header
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from app.utils.token_manager import TokenManager
from app.entities.dto.teacher_dto import TeacherReadDTO, TeacherPostRequest, TeacherUpdateDTO
from app.usecases.teachers_usecase import TeachersUseCase
from infrastructure.database.mysql.repository.teachers_respository import TeacherRepository
from infrastructure.database.mysql.repository.users_repository import UsersRepository
from infrastructure.email.sender import EmailSender

get_usecase = lambda: TeachersUseCase(
    teachers_repository=TeacherRepository(),
    users_repository=UsersRepository(),
    email_sender=EmailSender()
)

oauth2 = OAuth2PasswordBearer("http://localhost:8070/api/auth/authenticate")
router = APIRouter(prefix="/api/teacher", tags=["Teacher"])


def get_user_id(token = Depends(oauth2)):
    if not TokenManager.is_valid(token):
        return 0
    return TokenManager.decode(token)["user_id"]


@router.get("", status_code=status.HTTP_200_OK, response_model=list[TeacherReadDTO])
async def get_all_teachers(usecase: TeachersUseCase = Depends(get_usecase), user_id = Depends(get_user_id)):
    response = usecase.get_all_teachers(user_id=user_id)
    return JSONResponse(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers
    )


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=TeacherReadDTO)
async def get_all_teachers(id: int, usecase: TeachersUseCase = Depends(get_usecase), user_id = Depends(get_user_id)):
    response = usecase.get_teacher_by_id(id, user_id=user_id)
    return JSONResponse(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers
    )


@router.post("", status_code=status.HTTP_201_CREATED, response_model=TeacherReadDTO)
async def add_new_teacher(teacher_create: TeacherPostRequest, usecase: TeachersUseCase = Depends(get_usecase), user_id = Depends(get_user_id)) -> None:
    response = usecase.create_new_teacher(teacher_create, user_id=user_id)
    return JSONResponse(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers
    )


@router.put("", status_code=status.HTTP_200_OK, response_model=TeacherReadDTO)
async def update_teacher(update: TeacherUpdateDTO, usecase: TeachersUseCase = Depends(get_usecase), user_id = Depends(get_user_id)):
    response = usecase.update_teacher(update, user_id=user_id)
    return JSONResponse(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers
    )


@router.delete("", status_code=status.HTTP_200_OK)
async def delete_teacher(teacher_id = Header(alias="teacher_id"), usecase: TeachersUseCase = Depends(get_usecase), user_id = Depends(get_user_id)):
    response = usecase.delete_teacher(teacher_id, user_id=user_id)
    return JSONResponse(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers
    )
