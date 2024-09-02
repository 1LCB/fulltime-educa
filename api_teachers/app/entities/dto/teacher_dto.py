from pydantic import BaseModel, ConfigDict


class TeacherInsertInDatabaseDTO(BaseModel):
    name: str
    email: str
    cpf: str
    user_id: int


class TeacherReadDTO(BaseModel):
    id: int
    name: str
    email: str
    cpf: str
    user_id: int
    image_path: str | None = ""


class TeacherPostRequest(BaseModel):
    name: str
    email: str
    cpf: str
    image: str


class TeacherUpdateDTO(BaseModel):
    id: int
    name: str | None = None
    email: str | None = None
    cpf: str | None = None
