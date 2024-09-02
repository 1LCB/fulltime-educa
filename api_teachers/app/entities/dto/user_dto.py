from pydantic import BaseModel


class UserDTO(BaseModel):
    name: str
    email: str
    password: str
    group_id: int = 2
    image_path: str | None = None