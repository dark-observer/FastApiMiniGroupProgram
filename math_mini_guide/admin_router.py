from fastapi import APIRouter
from tortoise.models import Q
from starlette.requests import Request
from fastapi.responses import ORJSONResponse

from math_mini_guide.models import Area, Catalogue, Article, WechatUser
from math_mini_guide.pydantics import PydanticArea, PydanticCatalogue, PydanticArticle, PydanticWechatUser

router = APIRouter(prefix='/admin')
