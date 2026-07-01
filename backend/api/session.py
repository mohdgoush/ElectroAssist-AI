from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.dependencies import get_db
from backend.core.auth import get_current_user
from backend.models.user import User

from backend.services.session_service import (
    create_session,
    get_user_sessions,
    rename_session,
    delete_session,
    get_session
)
from backend.services.session_service import (
    get_or_create_session
)

from backend.models.chat_history import ChatHistory

router = APIRouter(
    tags=["Sessions"]
)


# =====================================================
# Request Models
# =====================================================

class CreateSessionRequest(BaseModel):
    session_name: str = "New Chat"


class RenameSessionRequest(BaseModel):
    session_name: str


# =====================================================
# Create New Session
# =====================================================

@router.post("/sessions")
def new_session(
    request: CreateSessionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    session = create_session(
        db=db,
        user_id=current_user.id,
        session_name=request.session_name
    )

    return {
        "id": session.id,
        "session_name": session.session_name
    }


# =====================================================
# Get All Sessions
# =====================================================

@router.get("/sessions")
def get_sessions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    sessions = get_user_sessions(
        db,
        current_user.id
    )

    return [
        {
            "id": s.id,
            "session_name": s.session_name,
            "created_at": s.created_at,
            "updated_at": s.updated_at
        }
        for s in sessions
    ]


# =====================================================
# Rename Session
# =====================================================

@router.patch("/sessions/{session_id}")
def rename_chat(
    session_id: int,
    request: RenameSessionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    session = get_session(
        db,
        session_id
    )

    if session is None:

        raise HTTPException(
            status_code=404,
            detail="Session not found."
        )

    if session.user_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="Unauthorized."
        )

    session = rename_session(
        db,
        session_id,
        request.session_name
    )

    return {
        "message": "Session renamed successfully."
    }


# =====================================================
# Delete Session
# =====================================================

@router.delete("/sessions/{session_id}")
def remove_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    session = get_session(
        db,
        session_id
    )

    if session is None:

        raise HTTPException(
            status_code=404,
            detail="Session not found."
        )

    if session.user_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="Unauthorized."
        )

    delete_session(
        db,
        session_id
    )

    return {
        "message": "Session deleted successfully."
    }
@router.post("/sessions/auto")
def auto_session(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    session = get_or_create_session(
        db,
        current_user.id
    )

    return {
        "id": session.id,
        "session_name": session.session_name
    }

@router.delete("/sessions/{session_id}/messages")
def clear_session_messages(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    session = get_session(
        db,
        session_id
    )

    if session is None:

        raise HTTPException(
            status_code=404,
            detail="Session not found."
        )

    if session.user_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="Unauthorized."
        )

    db.query(ChatHistory).filter(
        ChatHistory.session_id == session_id
    ).delete()

    db.commit()

    return {
        "message": "Chat history cleared successfully."
    }

@router.delete("/sessions")
def clear_all_sessions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    sessions = get_user_sessions(
        db,
        current_user.id
    )

    for session in sessions:

        db.query(ChatHistory).filter(
            ChatHistory.session_id == session.id
        ).delete()

        db.delete(session)

    db.commit()

    return {
        "message": "All chats deleted successfully."
    }
