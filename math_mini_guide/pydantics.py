from typing import Optional
from pydantic import BaseModel


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
    signature: Optional[str] = ''
