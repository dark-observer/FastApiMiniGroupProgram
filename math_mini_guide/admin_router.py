from fastapi import APIRouter
from tortoise.models import Q
from starlette.requests import Request
from fastapi.responses import ORJSONResponse

from math_mini_guide.models import Area, Catalogue, Article, WechatUser
from math_mini_guide.pydantics import PydanticArea, PydanticCatalogue, PydanticArticle, PydanticWechatUser

router = APIRouter(prefix='/admin')

MODEL_MAP = {
    'area': Area,
    'catalogue': Catalogue,
    'article': Article,
    'wechat_user': WechatUser
}

DAN_MAP = {
    'area': PydanticArea,
    'catalogue': PydanticCatalogue,
    'article': PydanticArticle,
    'wechat_user': PydanticWechatUser
}


@router.get('/{app_model}', response_class=ORJSONResponse)
async def model(request: Request, app_model: str):
    print(request.query_params.get('page'))
    print(request.query_params.get('size'))
    result = await MODEL_MAP[app_model].filter().offset(1).limit(20)
    return {
        'count': len(result),
        'result': result
    }
