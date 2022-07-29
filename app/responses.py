from fastapi import Response
from .schemas import ResponseModel

class UserResponseModel(ResponseModel):
    id: int
    name: str
    lastname: str
    email: str
    username: str

class UserTypeResponseModel(ResponseModel):
    id: str
    name: str
