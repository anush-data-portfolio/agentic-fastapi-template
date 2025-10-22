"""Application configuration loaded from environment variables."""

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the application."""

    PROJECT_NAME: str = "fastapi-app"
    ENV: str = "development"
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    SECRET_KEY: str = Field(default="")
    ENCRYPT_KEY: str = Field(default="")
    DATABASE_URL: str = "sqlite:///./app.db"
    GEMINI_API_KEY: str = Field(default="")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_TYPE: str = Field(default="bearer")

    # OAuth2
    GOOGLE_CLIENT_ID: str | None = None
    GOOGLE_CLIENT_SECRET: str | None = None
    GITHUB_CLIENT_ID: str | None = None
    GITHUB_CLIENT_SECRET: str | None = None
    GITHUB_ACCESS_TOKEN_URL: str | None = None

    FIRST_SUPERUSER_EMAIL: str = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = Field(default="")

    model_config = {"env_file": ".env"}


settings = Settings()
