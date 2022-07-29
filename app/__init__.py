from fastapi import FastAPI, APIRouter

from .core.database import database as connection
from .models.user import User, UserType
from .routes import *

from config import config

app = FastAPI(
    title = config.TITLE,
    description = config.DESCRIPTION,
    version = config.VERSION
)

api = APIRouter(prefix = '/api/v1')

api.include_router(user_router)

app.include_router(api)

@app.on_event('startup')
async def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([ User, UserType ])

@app.on_event('shutdown')
async def shutdown():
    if not connection.is_closed():
        connection.close()
