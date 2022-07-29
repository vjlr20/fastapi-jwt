import re

from pydantic import BaseModel, validator

class UserRequestModel(BaseModel):
    name: str
    lastname: str
    email: str
    password: str
    type: int

    @validator('email')
    def email_validator(cls, email):
        pattern = r"^(([^<>().,;:\s@”]+(\.[^<>().,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$";
        
        regex = re.search(pattern, email)

        if not regex:
            raise ValueError('Formato de correo electrónico no valido')

        return email

class UserTypeRequestModel(BaseModel):
    name: str

