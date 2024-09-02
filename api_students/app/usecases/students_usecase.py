from app.gateways.students_repository_gateway import StudentRepositoryGateway
from app.gateways.users_repository_gateway import UsersRepositoryGateway
from app.entities.http.http_response import HttpResponse
from app.entities.dto.student_dto import StudentCreate, StudentReadDTO, StudentUpdateDTO, StudentInsertInDatabase
from app.entities.dto.user_dto import UserDTO
from app.utils.hash_manager import HashManager
from http import HTTPStatus
import string, uuid, base64, random

# id=student.id,
#             user_id=student.user_id,
#             date_of_birth=student.date_of_birth,
#             gender=student.gender,
#             ethnicity=student.ethnicity,
#             birth_city=student.birth_city,
#             id_card=student.id_card,
#             cpf=student.cpf,
#             phone=student.phone,
#             address=student.address,
#             residential_complement=student.residential_complement,
#             father_name=student.father_name,
#             mother_name=student.mother_name,
#             school_attended=student.school_attended,
#             current_school=student.current_school,
#             shift=student.shift,
#             sector_id=student.sector_id,
#             admission_date=student.admission_date,
#             completion_date=student.completion_date,
#             course_status=student.course_status,
#             total_classes=student.total_classes,
#             attendances=student.attendances,
#             absences=student.absences,
#             name=student.name,
#             email=student.email,
#             image_path=student.image_path



# id=student.id,
#             user_id=student.user_id,
#             date_of_birth=student.date_of_birth,
#             gender=student.gender,
#             ethnicity=student.ethnicity,
#             birth_city=student.birth_city,
#             id_card=student.id_card,
#             cpf=student.cpf,
#             phone=student.phone,
#             address=student.address,
#             residential_complement=student.residential_complement,
#             father_name=student.father_name,
#             mother_name=student.mother_name,
#             school_attended=student.school_attended,
#             current_school=student.current_school,
#             shift=student.shift,
#             sector_id=student.sector_id,
#             admission_date=student.admission_date,
#             completion_date=student.completion_date,
#             course_status=student.course_status,
#             total_classes=student.total_classes,
#             attendances=student.attendances,
#             absences=student.absences
class StudentsUseCase:
    def __init__(
        self,
        students_repository: StudentRepositoryGateway,
        users_repository: UsersRepositoryGateway,
    ) -> None:
        self.students_repository = students_repository
        self.users_repository = users_repository

    def get_all_students(self) -> HttpResponse:
        students = self.students_repository.get_all_students()
        students_dto = [StudentReadDTO.model_validate(student).model_dump() for student in students]

        return HttpResponse(
            status_code=HTTPStatus.OK,
            content=students_dto,
        )
    
    def get_student_by_id(self, student_id: int) -> HttpResponse:
        student = self.students_repository.get_student_by_id(student_id)
        if student is None:
            return HttpResponse(
                status_code=HTTPStatus.NOT_FOUND,
                content={"detail": "student has not been found!"}
            )

        student_dto = StudentReadDTO.model_validate(student).model_dump()

        return HttpResponse(
            status_code=HTTPStatus.OK,
            content=student_dto
        )

    def create_new_student(self, student_create: StudentCreate):
        filename = self.save_photo(student_create.image)
        random_password = self.generate_random_password(10)

        print(f'RANDOM PASSWORD: {random_password}')

        random_password = HashManager.hash_password(random_password)
        user_id = self.users_repository.create_new_user(
            user=UserDTO(
                **student_create.model_dump(), 
                password=random_password, 
                image_path=filename
            )
        )

        t = StudentInsertInDatabase(**student_create.model_dump(), user_id=user_id)
        student_id = self.students_repository.insert_student(t)
        if student_id is None:
            return HttpResponse(
                content={"detail", "an error ocurred during the insertion process"},
                status_code=HTTPStatus.BAD_REQUEST,
            )
        
        s = self.students_repository.get_student_by_id(student_id)
        student_dto = StudentReadDTO.model_validate(s).model_dump()


        return HttpResponse(
            status_code=HTTPStatus.CREATED,
            content=student_dto
        )


    def delete_student(self, student_id: int):
        deleted = self.students_repository.delete_student_by_id(student_id)
        if not deleted:
            return HttpResponse(status_code=HTTPStatus.BAD_REQUEST, content={
                "detail": f"something went wrong when trying to delete student {student_id}"
            })
        return HttpResponse(
            status_code=HTTPStatus.OK,
            content={
                "info": f"student {student_id} deleted successfully"
            }
        )
    

    def update_student(self, student_update: StudentUpdateDTO):
        resp = self.students_repository.update_student(student_update)
        if resp is None:
            return HttpResponse(
                status_code=HTTPStatus.BAD_REQUEST,
                content={"detail": "something went wrong when trying to update user"}
            )
        return HttpResponse(
            status_code=HTTPStatus.OK,
            content={"id": resp["id"]}
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