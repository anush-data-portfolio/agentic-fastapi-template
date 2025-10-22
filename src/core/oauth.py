"""Configure reusable OAuth clients for external identity providers."""

from typing import Final

from authlib.integrations.starlette_client import OAuth

from src.core.config import settings

oauth = OAuth()

DEFAULT_GITHUB_OAUTH_ACCESS_ENDPOINT: Final[str] = (
    "https://github.com/login/oauth/access_token"
)

oauth.register(
    name="google",
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

oauth.register(
    name="github",
    client_id=settings.GITHUB_CLIENT_ID,
    client_secret=settings.GITHUB_CLIENT_SECRET,
    access_token_url=(
        settings.GITHUB_ACCESS_TOKEN_URL or DEFAULT_GITHUB_OAUTH_ACCESS_ENDPOINT
    ),
    access_token_params=None,
    authorize_url="https://github.com/login/oauth/authorize",
    authorize_params=None,
    api_base_url="https://api.github.com/",
    client_kwargs={"scope": "user:email"},
)
