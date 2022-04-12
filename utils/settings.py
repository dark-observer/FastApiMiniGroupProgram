DB_CONF = {
    'host': 'localhost',
    'port': '5432',
    'user': 'postgres',
    'password': 'Cr1yCarq1hR4DddYM76y',
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
