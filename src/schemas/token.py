"""Pydantic models describing OAuth2 token payloads."""

from pydantic import BaseModel


class Token(BaseModel):
    """Access token returned by the authentication endpoints."""

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Subset of token claims used during authentication."""

    email: str | None = None
