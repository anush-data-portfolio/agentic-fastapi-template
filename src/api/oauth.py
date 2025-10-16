from fastapi import APIRouter
from starlette.requests import Request

from src.core.oauth import oauth

router = APIRouter()


@router.get("/login/{provider}")
async def login(request: Request, provider: str):
    """
    Redirect to the provider's login page.

    Parameters
    ----------
    request : Request
        The request object.
    provider : str
        The OAuth provider.

    Returns
    -------
    RedirectResponse
        A redirect response to the provider's login page.
    """
    redirect_uri = request.url_for("auth", provider=provider)
    return await oauth.create_client(provider).authorize_redirect(request, redirect_uri)


@router.get("/auth/{provider}")
async def auth(request: Request, provider: str):
    """
    Handle the provider's callback.

    Parameters
    ----------
    request : Request
        The request object.
    provider : str
        The OAuth provider.

    Returns
    -------
    dict
        A dictionary containing the user information and the token.
    """
    token = await oauth.create_client(provider).authorize_access_token(request)
    user = await oauth.create_client(provider).parse_id_token(request, token)
    # Here you would typically create or update the user in your database
    # and create a JWT token for them.
    return {"user": user, "token": token}
