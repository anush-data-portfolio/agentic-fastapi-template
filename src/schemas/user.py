from pydantic import BaseModel


class UserBase(BaseModel):
    """
    Base user schema.
    """

    email: str


class UserCreate(UserBase):
    """
    User create schema.
    """

    password: str


class User(UserBase):
    """
    User schema.
    """

    id: int
    is_active: bool

    model_config = {"from_attributes": True}
