from backend.core.database import engine

from backend.models.base import Base

from backend.models.user import User
from backend.models.session import Session
from backend.models.chat_history import ChatHistory

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")