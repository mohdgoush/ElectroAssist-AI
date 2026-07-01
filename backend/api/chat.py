from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from backend.core.dependencies import get_db
from backend.core.auth import get_current_user

from backend.models.user import User
from backend.models.session import Session as ChatSession

from backend.services.chat_service import save_message

from backend.graph.graph_builder import app_graph
from backend.services.session_service import (
    get_user_session,
    auto_rename_session
)

router = APIRouter()


class ChatRequest(BaseModel):
    session_id: int
    message: str


@router.post("/chat")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # =====================================================
    # Verify Session
    # =====================================================

    session = get_user_session(
    db,
    request.session_id,
    current_user.id
)

    if session is None:

        raise HTTPException(
            status_code=404,
            detail="Chat session not found."
        )

    # =====================================================
    # Save User Message
    # =====================================================

    save_message(
        db=db,
        session_id=request.session_id,
        mode="chat",
        role="user",
        message=request.message
    )

    # =====================================================
    # AI Response
    # =====================================================

    result = app_graph.invoke(
        {
            "question": request.message,
            "user_id": current_user.id,
            "session_id": request.session_id
        }
    )

    answer = result["response"]

    # =====================================================
    # Save Assistant Message
    # =====================================================

    save_message(
        db=db,
        session_id=request.session_id,
        mode="chat",
        role="assistant",
        message=answer
    )

    return {
        "session_id": request.session_id,
        "response": answer
    }