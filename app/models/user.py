import datetime

from peewee import *

from ..core.database import database
from ..core.hashing import Hasher

class UserType(Model):
    name = CharField(max_length = 100, null = False)
    created_at = DateTimeField(default = datetime.datetime.now)
    updated_at = DateTimeField()

    class Meta:
        database = database
        table_name = 'user_types'

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        
        return super(UserType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class User(Model):
    name = CharField(max_length = 100, null = False)
    lastname = CharField(max_length = 200, null = False)
    username = CharField(max_length = 50, unique = True)
    email = CharField(max_length = 200, unique = True)
    password = CharField(max_length = 255, null = False)
    type = ForeignKeyField(UserType, null = False, on_delete='CASCADE')
    created_at = DateTimeField(default = datetime.datetime.now)
    updated_at = DateTimeField()

    class Meta:
        database = database
        table_name = 'users'

    @classmethod
    def authenticate(cls, username, password):
        user = cls.select().where(cls.username == username).first()

        hasher = Hasher()

        if user and hasher.verify_password(password, user.password):
            return user

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
