from peewee import *

from config import config

database = MySQLDatabase(config.DATABASE,
    user = config.USER,
    password = config.PASSWORD,
    host = config.HOST,
    port = config.PORT
)
