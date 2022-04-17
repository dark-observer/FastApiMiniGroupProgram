from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from math_mini_guide.router import router as math_mini_guide_router
from math_mini_guide.admin_router import router as admin_router
from math_mini_guide.models import WechatUser
from utils.reference import b64encode

from utils.settings import DATABASE, DATABASE_MODELS, CORS_ALLOW_ORIGINS

WHITELIST = [
    '/admin'
]

app = FastAPI()

# 解决跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(math_mini_guide_router)
app.include_router(admin_router)


@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    for white_list in WHITELIST:
        if request.url.path.startswith(white_list):
            return await call_next(request)

    if token := request.headers.get('Token'):
        payload, signature = token.split('.')
        count = await WechatUser.filter(open_id=b64encode(payload), signature=b64encode(signature)).count()
        if count > 0:
            return await call_next(request)

    return Response('身份未验证'.encode('GB18030'))


# 所有应用的model注册到数据库
register_tortoise(
    app,
    config={
        'connections': DATABASE,
        'apps': {
            'models': {
                'models': DATABASE_MODELS
            }
        },
        "use_tz": True,
        "timezone": "Asia/Shanghai"
    },
    generate_schemas=True
)
