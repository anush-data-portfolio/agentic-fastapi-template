"""Password hashing helpers and JWT token utilities."""

from datetime import datetime, timedelta, timezone
from typing import Any

from jose import jwt
from passlib.context import CryptContext

from src.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(
    data: dict[str, Any],
    expires_delta: timedelta | None = None,
) -> str:
    """Create a signed JWT access token for the provided payload.

    Parameters
    ----------
    data : dict[str, Any]
        Claims to encode into the resulting token.
    expires_delta : timedelta | None, optional
        Optional expiration interval; defaults to 15 minutes when omitted.

    Returns
    -------
    str
        Encoded JWT string suitable for use as a bearer token.

    """
    to_encode = data.copy()
    now = datetime.now(tz=timezone.utc)
    expire = now + expires_delta if expires_delta else now + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify that a plaintext password matches its hashed counterpart.

    Parameters
    ----------
    plain_password : str
        Password supplied by the user.
    hashed_password : str
        Stored password hash retrieved from persistence.

    Returns
    -------
    bool
        True when the password matches, otherwise False.

    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a plaintext password using the configured password context.

    Parameters
    ----------
    password : str
        Password requiring hashing.

    Returns
    -------
    str
        Resulting password hash safe for storage.

    """
    return pwd_context.hash(password)
