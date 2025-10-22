"""OAuth2 password grant endpoint for issuing access tokens."""

from datetime import timedelta
from typing import Annotated, Final

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.core import auth
from src.core.config import settings
from src.core.security import create_access_token, verify_password
from src.crud import user as user_crud
from src.schemas.token import Token

router = APIRouter()

TOKEN_TYPE: Final[str] = settings.ACCESS_TOKEN_TYPE


@router.post("/token")
def login_for_access_token(
    db: Annotated[Session, Depends(auth.get_db)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    """Issue an access token for a valid user credential exchange.

    Parameters
    ----------
    db : Session
        Database session provided by the authentication layer.
    form_data : OAuth2PasswordRequestForm
        Submitted login credentials from the OAuth2 password grant flow.

    Returns
    -------
    Token
        Serialized access token payload expected by API clients.

    Raises
    ------
    HTTPException
        Raised when the credentials are invalid or the user does not exist.

    """
    user = user_crud.get_user_by_email(db, email=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=auth.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type=TOKEN_TYPE)
