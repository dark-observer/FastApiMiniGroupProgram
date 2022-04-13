from fastapi import APIRouter
from tortoise.models import Q
from starlette.requests import Request

from math_mini_guide.models import Area, Catalogue, Article, WechatUser
from math_mini_guide.pydantics import PydanticArea, PydanticCatalogue, PydanticArticle, PydanticWechatUser

router = APIRouter()


@router.get('/full-area')
async def full_area():
    return await Area.all()


@router.post('/post-area/<pk>')
async def post_area(pk: int, area: PydanticArea):
    data = area.dict()
    if pk:
        area = await Area.get(pk=pk)
        await area.update_from_dict(data)
    else:
        area = await Area.create(**data)
    return area


@router.get('/full-catalogue')
async def full_catalogue(request: Request):
    q = Q()
    if area := request.query_params.get('area'):
        q &= Q(area_id=area)
    return await Catalogue.filter(q)


@router.post('/post-catalogue/<pk>')
async def post_catalogue(pk: int, catalogue: PydanticCatalogue):
    data = catalogue.dict()
    if pk:
        catalogue = await Catalogue.get(id=pk)
        await catalogue.update_from_dict(data)
    else:
        catalogue = await Catalogue.create(**data)
    return catalogue


@router.get('/full-article')
async def full_article(request: Request):
    q = Q()
    if area := request.query_params.get('area'):
        q &= Q(area_id=area)
    if catalogue := request.query_params.get('catalogue'):
        q &= Q(catalogue_id=catalogue)
    return await Article.filter(q)


@router.post('/post-article/<pk>')
async def post_article(pk: int, article: PydanticArticle):
    data = article.dict()
    if pk:
        article = await Article.get(id=pk)
        await article.update_from_dict(data)
    else:
        article = await Article.create(**data)
    return article


@router.get('/full-wechat_user')
async def full_wechat_user():
    return await WechatUser.all()


@router.post('/post-wechat_user/<pk>')
async def post_wechat_user(pk: int, wechat_user: PydanticWechatUser):
    data = wechat_user.dict()
    if pk:
        wechat_user = await WechatUser.get(id=pk)
        await wechat_user.update_from_dict(data)
    else:
        wechat_user = await WechatUser.create(**data)
    return wechat_user


@router.get('/test-amis')
async def test_amis():
    return {
        "status": 0,
        "msg": "",
        "data": {
            "title": "Test Page Component",
            "date": "2017-10-13"
        }
    }
