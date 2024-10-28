from fastapi import FastAPI, Request
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings, SettingsConfigDict
from src.api.routes import users
from src.api.routes import home
from src.api.routes import post

ALLOWED_HOSTS = [
    "https://social-network-front-production-f940.up.railway.app",
    "http://localhost:5000", # dev front
]

class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=('.env.prod', '.env'),
        env_file_encoding='utf-8'
    )

app_settings = Settings()

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
                'default': app_settings.DATABASE_URL
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