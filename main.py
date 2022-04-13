from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise

from math_mini_guide.router import router as math_mini_guide_router
from utils.settings import DATABASE, DATABASE_MODELS, CORS_ALLOW_ORIGINS, BASE_DIR

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

# 静态文件挂载目录
app.mount('/amis', StaticFiles(directory=BASE_DIR.joinpath('admin').joinpath('amis')), name='amis')
# 模板文件挂载目录
admin_template = Jinja2Templates(directory=BASE_DIR.joinpath('admin'))

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



@app.route('/admin')
async def admin_index(request):
    return admin_template.TemplateResponse('index.html', {'request': request})