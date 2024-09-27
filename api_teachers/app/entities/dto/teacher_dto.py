from pydantic import BaseModel, ConfigDict


class TeacherInsertInDatabaseDTO(BaseModel):
    name: str
    email: str
    address: str
    phone: str
    user_id: int


class TeacherReadDTO(BaseModel):
    id: int
    name: str
    email: str
    address: str | None = ""
    phone: str | None = ""
    user_id: int
    image_path: str | None = ""


class TeacherPostRequest(BaseModel):
    name: str
    email: str
    address: str
    phone: str
    image: str


class TeacherUpdateDTO(BaseModel):
    id: int
    name: str | None = None
    email: str | None = None
    address: str | None = None
    phone: str | None = None
