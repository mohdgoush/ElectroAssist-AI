from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    sessions = relationship("Session", back_populates="user", cascade="all, delete-orphan")