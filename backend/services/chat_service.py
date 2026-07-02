from sqlalchemy.orm import Session
from backend.models.chat_history import ChatHistory
from backend.models.session import Session as ChatSession

def save_message(
    db: Session,
    session_id: int,
    mode: str,
    role: str,
    message: str
):

    session = db.query(ChatSession).filter(ChatSession.id == session_id).first()

    if session is None:
        return None

    chat = ChatHistory(
        session_id=session_id,
        mode=mode,
        role=role,
        message=message
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat

def get_session_messages(db: Session, session_id: int):
    return db.query(ChatHistory).filter(ChatHistory.session_id == session_id).order_by(ChatHistory.created_at.asc()).all()