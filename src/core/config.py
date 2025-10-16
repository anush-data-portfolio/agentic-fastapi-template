from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the application.
    """

    PROJECT_NAME: str = "fastapi-app"
    ENV: str = "development"
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    SECRET_KEY: str = "change_me_to_a_random_64_char_string"
    ENCRYPT_KEY: str = "change_me_to_a_random_44_char_base64_string"
    DATABASE_URL: str = "sqlite:///./app.db"
    GEMINI_API_KEY: str = "put_your_google_generative_ai_key_here"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"

    # OAuth2
    GOOGLE_CLIENT_ID: str | None = None
    GOOGLE_CLIENT_SECRET: str | None = None
    GITHUB_CLIENT_ID: str | None = None
    GITHUB_CLIENT_SECRET: str | None = None

    FIRST_SUPERUSER_EMAIL: str = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "password"

    model_config = {"env_file": ".env"}


settings = Settings()
