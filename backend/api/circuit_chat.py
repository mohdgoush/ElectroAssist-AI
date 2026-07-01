from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from backend.core.dependencies import get_db
from backend.core.auth import get_current_user

from backend.models.user import User
from backend.models.session import Session as ChatSession

from backend.services.chat_service import save_message

from backend.agents.circuit_chat_agent import (
    circuit_chat_agent
)
from backend.services.session_service import (
    get_user_session,
    auto_rename_session
)

router = APIRouter()


class CircuitChatRequest(BaseModel):
    session_id: int
    question: str
    analysis: str


@router.post("/circuit-chat")
def circuit_chat(
    request: CircuitChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # =====================================================
    # Verify Session
    # =====================================================

    session = (
        db.query(ChatSession)
        .filter(
            ChatSession.id == request.session_id,
            ChatSession.user_id == current_user.id
        )
        .first()
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
        mode="circuit",
        role="user",
        message=request.question
    )

    auto_rename_session(
    db,
    request.session_id,
    request.question
)

    # =====================================================
    # AI Response
    # =====================================================

    answer = circuit_chat_agent(
        question=request.question,
        analysis=request.analysis,
        session_id=request.session_id
    )

    # =====================================================
    # Save Assistant Message
    # =====================================================

    save_message(
        db=db,
        session_id=request.session_id,
        mode="circuit",
        role="assistant",
        message=answer
    )

    # =====================================================
    # Debug Log
    # =====================================================

    print("\n========== CIRCUIT CHAT ==========")
    print("USER:", current_user.username)
    print("SESSION:", request.session_id)
    print("QUESTION:", request.question)
    print("ANALYSIS:", request.analysis[:500])
    print("ANSWER:", answer)
    print("==================================\n")

    return {
        "session_id": request.session_id,
        "response": answer
    }