from sqlalchemy.orm import Session

from src.core.security import get_password_hash
from src.models.user import User
from src.schemas.user import UserCreate


def get_user_by_email(db: Session, email: str) -> User | None:
    """
    Get user by email.

    Parameters
    ----------
    db : Session
        Database session.
    email : str
        User email.

    Returns
    -------
    User | None
        User or None.
    """
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate) -> User:
    """
    Create user.

    Parameters
    ----------
    db : Session
        Database session.
    user : UserCreate
        User create schema.

    Returns
    -------
    User
        User.
    """
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
