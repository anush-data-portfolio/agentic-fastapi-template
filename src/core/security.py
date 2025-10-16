from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from src.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Create access token.

    Parameters
    ----------
    data : dict
        Data to encode.
    expires_delta : timedelta | None, optional
        Expires delta, by default None.

    Returns
    -------
    str
        Access token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify password.

    Parameters
    ----------
    plain_password : str
        Plain password.
    hashed_password : str
        Hashed password.

    Returns
    -------
    bool
        True if password is correct, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Get password hash.

    Parameters
    ----------
    password : str
        Password.

    Returns
    -------
    str
        Hashed password.
    """
    return pwd_context.hash(password)
