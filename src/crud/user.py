"""User persistence helpers built on SQLAlchemy sessions."""

from sqlalchemy.orm import Session

from src.core.security import get_password_hash
from src.models.user import User
from src.schemas.user import UserCreate


def get_user_by_email(db: Session, email: str) -> User | None:
    """Retrieve a user by email address, if one exists.

    Parameters
    ----------
    db : Session
        Active database session.
    email : str
        Email address used to look up the user.

    Returns
    -------
    User | None
        Matching user instance or None when absent.

    """
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate) -> User:
    """Persist a new user with a securely hashed password.

    Parameters
    ----------
    db : Session
        Active database session.
    user : UserCreate
        Schema containing the user information to persist.

    Returns
    -------
    User
        Newly created database user model.

    """
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
