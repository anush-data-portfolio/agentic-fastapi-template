"""Dependencies for authenticating requests against the local user database."""

from collections.abc import Generator
from typing import Annotated, Any

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from src.core.config import settings
from src.crud import user as user_crud
from src.db.session import SessionLocal
from src.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login/token")


def get_db() -> Generator[Session, None, None]:
    """Yield a SQLAlchemy session tied to the current request lifecycle.

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
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)],
) -> User:
    """Resolve the currently authenticated user from a JWT bearer token.

    Parameters
    ----------
    token : str
        Encoded JWT provided by the OAuth2 password grant.
    db : Session
        Database session used to retrieve the persisted user.

    Returns
    -------
    User
        Database user model associated with the provided token.

    Raises
    ------
    HTTPException
        Raised when the token is invalid or the referenced user does not exist.

    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload: dict[str, Any]
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
    except JWTError as exc:
        raise credentials_exception from exc

    subject_claim = payload.get("sub")
    if not isinstance(subject_claim, str):
        raise credentials_exception
    subject = subject_claim

    user = user_crud.get_user_by_email(db, email=subject)
    if user is None:
        raise credentials_exception
    return user
