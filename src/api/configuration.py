from fastapi import FastAPI, Request
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import users
from src.api.routes import home
from src.api.routes import post

ALLOWED_HOSTS = [
    "http://127.0.0.1:5500",
]

def configure_routes(app: FastAPI):
    home_show(app)
    app.include_router(users.router)
    app.include_router(home.router)
    app.include_router(post.router)

def configure_db(app: FastAPI):
    register_tortoise(
        app=app,
        config={
            'connections': {
                # 'default': 'postgres://postgres:qwerty123@localhost:5432/events'
                'default': 'sqlite://db.sqlite3'
            },
            'apps': {
                'models': {
                    'models': [
                        'src.datalayer.models.user',
                        'src.datalayer.models.post',
                    ],
                    'default_connection': 'default',
                }
            }
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )

def configure_middlewares(app):

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def home_show(app):
    from fastapi.templating import Jinja2Templates
    templates = Jinja2Templates(directory="templates")
    @app.get('/')
    async def home_show(request: Request):
        return templates.TemplateResponse(
            request=request, name="index.html"
        )