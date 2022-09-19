import random

from fastapi import APIRouter, HTTPException, Depends
from typing import List

from ..models.user import User, UserType
from ..requests import *
from ..responses import *

from ..core.hashing import Hasher
from ..common import oauth2_schema

router = APIRouter(prefix = '/users')

@router.get('', response_model = List[UserResponseModel])
async def index(token: str = Depends(oauth2_schema)):
    users = User.select()

    return [user for user in users]

@router.post('', response_model = UserResponseModel)
async def store(request: UserRequestModel, token: str = Depends(oauth2_schema)):
    if User.select().where(User.email == request.email).first():
        raise HTTPException(409, 'El correo electrónico ya se encuentra en uso.')

    random_number = '{:03d}'.format(random.randrange(1, 999))
    
    first_letter = request.name[0][0]
    first_letter_lastname = request.lastname[0:5]

    username = '{}.{}{}'.format(first_letter, first_letter_lastname, random_number)

    hash_password = Hasher.get_password_hash(request.password)

    user =  User(
        name = request.name,
        lastname = request.lastname,
        username = username.lower(),
        email = request.email,
        password = hash_password,
        type = request.type
    )
    user.save()

    return user

@router.post('/types', response_model = UserTypeResponseModel)
async def new_type(request: UserTypeRequestModel):
    type = UserType(
        name = request.name
    )
    type.save()

    return type

