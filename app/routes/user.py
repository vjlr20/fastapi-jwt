import random

from fastapi import APIRouter, HTTPException
from typing import List

from ..models.user import User
from ..requests import *
from ..responses import *

from ..core.hashing import Hasher

router = APIRouter(prefix = '/users')

@router.get('', response_model = List[UserResponseModel])
async def index():
    users = User.select()

    return [user for user in users]

@router.post('', response_model = UserResponseModel)
async def store(request: UserRequestModel):
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
        password = hash_password
    )
    user.save()

    return user

