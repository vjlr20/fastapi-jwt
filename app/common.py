import jwt, datetime

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from .models.user import User

SECRET_KEY = 'BootcampAPI2022'

oauth2_schema = OAuth2PasswordBearer(tokenUrl = '/api/v1/auth/login')

def create_access_token(user, days = 7):
    data = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days = days)
    }

    return jwt.encode(data, SECRET_KEY, algorithm = 'HS256')

def decode_access_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms = ['HS256'])
    except Exception as err:
        return None

def get_current_user(token: str = Depends(oauth2_schema)) -> User:
    data = decode_access_token(token)

    if data:
        return User.get(id = data['user_id'])
    else:
        raise HTTPException(
            status_code = 401, 
            detail = 'Access token no valido',
            headers = {'WWW-Authenticate': 'Bearer'}
        )

def revoke_access_token(token: str = Depends(oauth2_schema)):
    pass
