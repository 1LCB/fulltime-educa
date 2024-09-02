from fastapi import APIRouter, status, Depends, Header
from fastapi.responses import JSONResponse
from app.entities.dto.student_dto import StudentReadDTO, StudentCreate, StudentUpdateDTO
from app.usecases.students_usecase import StudentsUseCase
from infrastructure.database.mysql.repository.students_respository import StudentRepository
from infrastructure.database.mysql.repository.users_repository import UsersRepository


get_usecase = lambda: StudentsUseCase(
    students_repository=StudentRepository(),
    users_repository=UsersRepository()
)

router = APIRouter(prefix="/api/student", tags=["student"])


@router.get("", status_code=status.HTTP_200_OK, response_model=list[StudentReadDTO])
async def get_all_students(usecase: StudentsUseCase = Depends(get_usecase)):
    response = usecase.get_all_students()
    return JSONResponse(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers
    )


@router.get("{id}", status_code=status.HTTP_200_OK, response_model=list[StudentReadDTO])
async def get_student_by_id(id: int, usecase: StudentsUseCase = Depends(get_usecase)):
    response = usecase.get_student_by_id(id)
    return JSONResponse(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers
    )


@router.post("", status_code=status.HTTP_201_CREATED)
async def add_new_student(student_create: StudentCreate, usecase: StudentsUseCase = Depends(get_usecase)) -> StudentReadDTO:
    response = usecase.create_new_student(student_create)
    return JSONResponse(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers
    )


@router.put("", status_code=status.HTTP_200_OK)
async def update_student(update: StudentUpdateDTO, usecase: StudentsUseCase = Depends(get_usecase)) -> StudentReadDTO:
    response = usecase.update_student(update)
    return JSONResponse(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers
    )


@router.delete("", status_code=status.HTTP_200_OK)
async def delete_student(student_id = Header(alias="student_id"), usecase: StudentsUseCase = Depends(get_usecase)) -> str:
    response = usecase.delete_student(student_id)
    return JSONResponse(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers
    )
