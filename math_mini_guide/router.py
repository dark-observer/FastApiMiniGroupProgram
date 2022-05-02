from fastapi import APIRouter
from tortoise.models import Q
from starlette.requests import Request
from fastapi.responses import ORJSONResponse

from math_mini_guide.models import Area, Catalogue, Article, WechatUser
from math_mini_guide.pydantics import PydanticArea, PydanticCatalogue, PydanticArticle, PydanticWechatUser

router = APIRouter()


@router.get('/full-area', response_class=ORJSONResponse)
async def full_area():
    return await Area.all()


@router.get('/full-catalogue', response_class=ORJSONResponse)
async def full_catalogue(request: Request):
    q = Q()
    if area := request.query_params.get('area'):
        q &= Q(area_id=area)
    return await Catalogue.filter(q)


@router.get('/full-article', response_class=ORJSONResponse)
async def full_article(request: Request):
    q = Q()
    if area := request.query_params.get('area'):
        q &= Q(area_id=area)
    if catalogue := request.query_params.get('catalogue'):
        q &= Q(catalogue_id=catalogue)
    return await Article.filter(q)


@router.get('/full-wechat_user', response_class=ORJSONResponse)
async def full_wechat_user():
    return await WechatUser.all()
