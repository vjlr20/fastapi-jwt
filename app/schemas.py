from typing import Any
from pydantic import BaseModel
from peewee import ModelSelect

from pydantic.utils import GetterDict

class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)

        if isinstance(res, ModelSelect):
            return list(res)

        return res

class ResponseModel(BaseModel):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

