from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from src.core.config import settings
from src.crud import user as user_crud
from src.db.session import SessionLocal
from src.models.user import User
from src.schemas.token import TokenData


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login/token")


def get_db():
    """
    Get database session.

    Yields
    ------
    Session
        Database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    """
    Get current user.

    Parameters
    ----------
    token : str, optional
        Token, by default Depends(oauth2_scheme).
    db : Session, optional
        Database session, by default Depends(get_db).

    Returns
    -------
    User
        User.

    Raises
    ------
    HTTPException
        If user is not found or token is invalid.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = user_crud.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user
