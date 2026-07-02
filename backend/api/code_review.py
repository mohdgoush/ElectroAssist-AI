from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from backend.core.dependencies import get_db
from backend.core.auth import get_current_user
from backend.models.user import User
from backend.models.session import Session as ChatSession
from backend.services.chat_service import save_message
from backend.agents.code_review_agent import code_review_agent
from backend.services.session_service import get_user_session, auto_rename_session

router = APIRouter()

class CodeReviewRequest(BaseModel):
    session_id: int
    message: str

@router.post("/review-code")
def review_code(request: CodeReviewRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    session = db.query(ChatSession).filter(ChatSession.id == request.session_id, ChatSession.user_id == current_user.id).first()

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Chat session not found."
        )
    
    save_message(
        db=db,
        session_id=request.session_id,
        mode="code",
        role="user",
        message=request.message
    )
    auto_rename_session(db, request.session_id, request.message)
    review = code_review_agent(request.message)

    save_message(
        db=db,
        session_id=request.session_id,
        mode="code",
        role="assistant",
        message=review
    )
    return {
        "session_id": request.session_id,
        "review": review
    }