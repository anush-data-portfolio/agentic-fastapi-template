from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.core import auth
from src.core.security import create_access_token, verify_password
from src.crud import user as user_crud
from src.schemas.token import Token

router = APIRouter()


@router.post("/token", response_model=Token)
def login_for_access_token(
    db: Session = Depends(auth.get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    """
    Login for access token.

    Parameters
    ----------
    db : Session, optional
        Database session, by default Depends(auth.get_db).
    form_data : OAuth2PasswordRequestForm, optional
        Form data, by default Depends().

    Returns
    -------
    Token
        Access token.

    Raises
    ------
    HTTPException
        If user is not found or password is not correct.
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
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
