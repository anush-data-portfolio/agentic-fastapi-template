"""OAuth redirect and callback handlers for third-party providers."""

from typing import Any

from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import Response

from src.core.oauth import oauth

router = APIRouter()


@router.get("/login/{provider}")
async def login(request: Request, provider: str) -> Response:
    """Redirect to the selected OAuth provider for authentication.

    Parameters
    ----------
    request : Request
        The inbound HTTP request initiating the OAuth login.
    provider : str
        The OAuth provider identifier registered with the application.

    Returns
    -------
    Response
        Redirect response that sends the user to the provider's login page.

    """
    redirect_uri = request.url_for("auth", provider=provider)
    return await oauth.create_client(provider).authorize_redirect(request, redirect_uri)


@router.get("/auth/{provider}")
async def auth(request: Request, provider: str) -> dict[str, Any]:
    """Handle the OAuth provider callback and normalize the token payload.

    Parameters
    ----------
    request : Request
        The inbound HTTP request received from the OAuth provider callback.
    provider : str
        The OAuth provider identifier registered with the application.

    Returns
    -------
    dict[str, Any]
        Dictionary containing the identity information and provider token payload.

    """
    token = await oauth.create_client(provider).authorize_access_token(request)
    user = await oauth.create_client(provider).parse_id_token(request, token)
    # Here you would typically create or update the user in your database
    # and create a JWT token for them.
    return {"user": user, "token": token}
