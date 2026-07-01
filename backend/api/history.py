from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.dependencies import get_db
from backend.core.auth import get_current_user

from backend.models.user import User
from backend.models.session import Session as ChatSession
from backend.models.chat_history import ChatHistory

router = APIRouter(tags=["History"])


@router.get("/sessions/{session_id}/messages")
def get_chat_history(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # =====================================================
    # Verify Session Ownership
    # =====================================================

    session = (
        db.query(ChatSession)
        .filter(
            ChatSession.id == session_id,
            ChatSession.user_id == current_user.id
        )
        .first()
    )

    if session is None:

        raise HTTPException(
            status_code=404,
            detail="Session not found."
        )

    # =====================================================
    # Get Messages
    # =====================================================

    messages = (
        db.query(ChatHistory)
        .filter(ChatHistory.session_id == session_id)
        .order_by(ChatHistory.created_at.asc())
        .all()
    )

    return [
        {
            "id": message.id,
            "role": message.role,
            "mode": message.mode,
            "message": message.message,
            "created_at": message.created_at
        }
        for message in messages
    ]