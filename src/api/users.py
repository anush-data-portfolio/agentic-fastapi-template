from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.core import auth
from src.crud import user as user_crud
from src.schemas import user as user_schema

router = APIRouter()


@router.post("/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(auth.get_db)):
    """
    Create user.

    Parameters
    ----------
    user : user_schema.UserCreate
        User create schema.
    db : Session, optional
        Database session, by default Depends(auth.get_db).

    Returns
    -------
    user_schema.User
        User.

    Raises
    ------
    HTTPException
        If user with this email already exists.
    """
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)


@router.get("/me", response_model=user_schema.User)
def read_users_me(current_user: user_schema.User = Depends(auth.get_current_user)):
    """
    Get current user.

    Parameters
    ----------
    current_user : user_schema.User, optional
        Current user, by default Depends(auth.get_current_user).

    Returns
    -------
    user_schema.User
        User.
    """
    return current_user
