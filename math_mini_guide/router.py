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


@router.post('/post-area/{pk}', response_class=ORJSONResponse)
async def post_area(pk: int, area: PydanticArea):
    await Area.update_or_create(area.dict(), pk=pk)
    return {
        'status': 0,
        'msg': '',
        'data': area
    }


@router.get('/full-catalogue', response_class=ORJSONResponse)
async def full_catalogue(request: Request):
    q = Q()
    if area := request.query_params.get('area'):
        q &= Q(area_id=area)
    return await Catalogue.filter(q)


@router.post('/post-catalogue/{pk}', response_class=ORJSONResponse)
async def post_catalogue(pk: int, catalogue: PydanticCatalogue):
    await Catalogue.update_or_create(catalogue.dict(), pk=pk)
    return catalogue


@router.get('/full-article', response_class=ORJSONResponse)
async def full_article(request: Request):
    q = Q()
    if area := request.query_params.get('area'):
        q &= Q(area_id=area)
    if catalogue := request.query_params.get('catalogue'):
        q &= Q(catalogue_id=catalogue)
    return await Article.filter(q)


@router.post('/post-article/{pk}', response_class=ORJSONResponse)
async def post_article(pk: int, article: PydanticArticle):
    data = article.dict()
    if pk:
        article = await Article.get(id=pk)
        await article.update_from_dict(data)
    else:
        article = await Article.create(**data)
    return article


@router.get('/full-wechat_user', response_class=ORJSONResponse)
async def full_wechat_user():
    return await WechatUser.all()


@router.post('/post-wechat_user/{pk}', response_class=ORJSONResponse)
async def post_wechat_user(pk: int, wechat_user: PydanticWechatUser):
    data = wechat_user.dict()
    if pk:
        wechat_user = await WechatUser.get(id=pk)
        await wechat_user.update_from_dict(data)
    else:
        wechat_user = await WechatUser.create(**data)
    return wechat_user
