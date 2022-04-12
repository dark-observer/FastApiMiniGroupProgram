from typing import Optional
from pydantic import BaseModel

from utils.reference import random_string


class PydanticArea(BaseModel):
    name: str
    no: Optional[int] = 0


class PydanticCatalogue(BaseModel):
    name: str
    area_id: int
    no: Optional[int] = 0


class PydanticArticle(BaseModel):
    name: str
    catalogue_id: int
    area_id: int
    body: Optional[str] = ''


class PydanticWechatUser(BaseModel):
    open_id = str
    signature: Optional[str] = random_string()

# class WechatUser(Model):
#     id = fields.IntField(pk=True)
#     open_id = fields.CharField(description="OpenID", max_length=50, unique=True)
#     signature = fields.CharField(description="签名", max_length=50, default=random_string())
