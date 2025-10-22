"""Routes for managing user resources and retrieving the active profile."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.core import auth
from src.crud import user as user_crud
from src.models.user import User
from src.schemas import user as user_schema

router = APIRouter()


@router.post("/", response_model=user_schema.User)
def create_user(
    user: user_schema.UserCreate,
    db: Annotated[Session, Depends(auth.get_db)],
) -> user_schema.User:
    """Create a new user record after validating uniqueness constraints.

    Parameters
    ----------
    user : user_schema.UserCreate
        Pydantic schema containing the registration payload.
    db : Session
        Database session provided by the authentication dependency.

    Returns
    -------
    user_schema.User
        Serialized user model representing the persisted entity.

    Raises
    ------
    HTTPException
        Raised when another account already uses the provided email address.

    """
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    created_user = user_crud.create_user(db=db, user=user)
    return user_schema.User.model_validate(created_user)


@router.get("/me", response_model=user_schema.User)
def read_users_me(
    current_user: Annotated[User, Depends(auth.get_current_user)],
) -> user_schema.User:
    """Return the authenticated user's profile information.

    Parameters
    ----------
    current_user : User
        Database model representing the authenticated user.

    Returns
    -------
    user_schema.User
        Serialized user schema.

    """
    return user_schema.User.model_validate(current_user)
