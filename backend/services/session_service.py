from sqlalchemy.orm import Session
from backend.models.session import Session as ChatSession

def create_session(
    db: Session,
    user_id: int,
    session_name: str = "New Chat"
):

    session = ChatSession(user_id=user_id, session_name=session_name)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session

def get_session(db: Session, session_id: int):
    return db.query(ChatSession).filter(ChatSession.id == session_id).first()

def get_user_session(db: Session, session_id: int, user_id: int):
    return db.query(ChatSession).filter(ChatSession.id == session_id, ChatSession.user_id == user_id).first()

def get_user_sessions(db: Session,user_id: int):
    return db.query(ChatSession).filter(ChatSession.user_id == user_id).order_by(ChatSession.updated_at.desc()).all()

def get_latest_session(db: Session, user_id: int):
    return db.query(ChatSession).filter(ChatSession.user_id == user_id).order_by(ChatSession.updated_at.desc()).first()

def get_or_create_session(db: Session, user_id: int):

    session = get_latest_session(db, user_id)
    if session:
        return session
    return create_session(db, user_id, "New Chat")

def rename_session(
    db: Session,
    session_id: int,
    session_name: str
):

    session = get_session(db, session_id)

    if session is None:
        return None

    session.session_name = session_name
    db.commit()
    db.refresh(session)
    return session

def delete_session(db: Session, session_id: int):

    session = get_session(db, session_id)
    if session is None:
        return False

    db.delete(session)
    db.commit()
    return True

def auto_rename_session(db: Session, session_id: int, first_message: str):

    session = get_session(db, session_id)
    if session is None:
        return

    if session.session_name != "New Chat":
        return

    title = first_message.strip()

    if len(title) > 40:
        title = title[:40].rstrip() + "..."

    session.session_name = title
    db.commit()