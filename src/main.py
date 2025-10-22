"""Initialize the FastAPI application and register API routers."""

from fastapi import FastAPI

from src.api import login, oauth, users
from src.core.config import settings
from src.db.base import Base
from src.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
)

app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(login.router, prefix="/api/login", tags=["login"])
app.include_router(oauth.router, prefix="/api/oauth", tags=["oauth"])
