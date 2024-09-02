from pydantic import BaseModel


class UserDTO(BaseModel):
    name: str
    email: str
    password: str
    group_id: int = 1
    image_path: str = ""
