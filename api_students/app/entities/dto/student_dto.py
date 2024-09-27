from pydantic import BaseModel, ConfigDict, validator
import datetime


class StudentCreate(BaseModel):
    name: str
    email: str
    # password: str
    date_of_birth: str = "2024-01-01"
    gender: str
    ethnicity: str
    birth_city: str
    id_card: str
    cpf: str
    phone: str
    address: str
    residential_complement: str
    father_name: str
    mother_name: str
    school_attended: int
    current_school: int
    shift: str
    sector_id: int
    admission_date: str
    completion_date: str
    course_status: str
    total_classes: int = 0
    attendances: int = 0
    absences: int = 0
    image: str = ""


class StudentInsertInDatabase(BaseModel):
    user_id: int
    date_of_birth: str
    gender: str
    ethnicity: str
    birth_city: str
    id_card: str
    cpf: str
    phone: str
    address: str
    residential_complement: str
    father_name: str
    mother_name: str
    school_attended: int
    current_school: int
    shift: str
    sector_id: int
    admission_date: str
    completion_date: str
    course_status: str
    total_classes: int
    attendances: int
    absences: int


class StudentReadDTO(BaseModel):
    id: int
    user_id: int
    date_of_birth: str 
    gender: str
    ethnicity: str
    birth_city: str
    id_card: str
    cpf: str
    phone: str
    address: str
    residential_complement: str
    father_name: str
    mother_name: str
    school_attended: int
    current_school: int
    shift: str
    sector_id: int
    admission_date: str
    completion_date: str
    course_status: str
    total_classes: int
    attendances: int
    absences: int
    name: str
    email: str
    image_path: str

    class Config:
        from_attributes=True

    @validator('date_of_birth', 'admission_date', 'completion_date', pre=True)
    def date_to_string(cls, v):
        if isinstance(v, datetime.date):
            return v.strftime('%Y-%m-%d')
        return v


class StudentUpdateDTO(BaseModel):
    id: int
    user_id: int
    date_of_birth: str
    gender: str
    ethnicity: str
    birth_city: str
    id_card: str
    cpf: str
    phone: str
    address: str
    residential_complement: str
    father_name: str
    mother_name: str
    school_attended: int
    current_school: int
    shift: str
    sector_id: int
    admission_date: str
    completion_date: str
    course_status: str
    total_classes: int
    attendances: int
    absences: int
