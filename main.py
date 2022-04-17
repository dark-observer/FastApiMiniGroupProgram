from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from math_mini_guide.router import router as math_mini_guide_router
from math_mini_guide.admin_router import router as admin_router

from utils.settings import DATABASE, DATABASE_MODELS, CORS_ALLOW_ORIGINS

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
