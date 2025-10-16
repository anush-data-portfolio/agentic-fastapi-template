from sqlalchemy import Boolean, Column, Integer, String

from src.db.base import Base


class User(Base):
    """
    User model.
    """

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
