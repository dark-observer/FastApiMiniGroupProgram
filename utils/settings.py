import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.absolute()

DB_CONF = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': '5432',
    'user': 'postgres',
    'password': os.getenv('DB_PASSWORD', '123456'),
    'database': 'math_mini_guide',
}

DATABASE = {
    'default': {
        'engine': 'tortoise.backends.asyncpg',
        'credentials': DB_CONF
    }
}

DATABASE_MODELS = [
    'math_mini_guide.models'
]

TORTOISE_ORM = {
    'connections': {
        'default': f"postgres://{DB_CONF['user']}:"
                   f"{DB_CONF['password']}@{DB_CONF['host']}:"
                   f"{DB_CONF['port']}/{DB_CONF['database']}"
    },
    'apps': {
        'models': {
            'models': ['aerich.models'] + DATABASE_MODELS,
            'default_connection': 'default'
        }
    }
}

CORS_ALLOW_ORIGINS = [
    '*'
]
