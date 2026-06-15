from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI shop"
    debug: bool = True
    database_url: str = "sqlite:/// ./shop.db"
    cors_origin: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:3000",
    ]
    static_dir: str = "static"
    image_dir: str = "static/images"

    class Config:
        env_file = ".env"


settings = Settings()
