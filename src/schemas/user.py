"""Pydantic representations of user data transfer objects."""

from pydantic import BaseModel


class UserBase(BaseModel):
    """Shared attributes exposed for user-facing payloads."""

    email: str


class UserCreate(UserBase):
    """Payload required to register a new user."""

    password: str


class User(UserBase):
    """Response model returned for persisted users."""

    id: int
    is_active: bool

    model_config = {"from_attributes": True}
