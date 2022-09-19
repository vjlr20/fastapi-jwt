from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from typing import List

from ..models.user import User, UserType

from ..common import create_access_token, get_current_user
from ..requests import *
from ..responses import *

router = APIRouter(prefix = '/auth')

async def register():
    pass

@router.post('/login')
async def login(data: OAuth2PasswordRequestForm = Depends()):
    user = User.authenticate(data.username, data.password)

    if user:
        return {
            'access_token': create_access_token(user),
            'token_type': 'Bearer',
        }
    else:
        raise HTTPException(
            status_code = 401, 
            detail = 'Nombre de usuario o contraseña incorrectos',
            headers = {'WWW-Authenticate': 'Bearer'}
        )

@router.get('/profile')
async def profile(user: User = Depends(get_current_user)):
    return {
        'id': user.id,
        'name': user.name,
        'lastname': user.lastname,
        'username': user.username,
        'email': user.email,
        'type': user.type.name
    }

# @router.get('/logout')
async def logout():
    pass
