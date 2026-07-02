from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.core.dependencies import get_db
from backend.core.auth import get_current_user
from backend.models.user import User
from backend.models.session import Session as ChatSession
from backend.services.chat_service import save_message
from backend.agents.pdf_chat_agent import pdf_chat_agent
from backend.services.session_service import get_user_session, auto_rename_session

router = APIRouter()

class PDFQuestion(BaseModel):
    session_id: int
    question: str


@router.post("/pdf-chat")
def ask_pdf(request: PDFQuestion, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    session = get_user_session(db, request.session_id, current_user.id)
    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Chat session not found."
        )
    save_message(
        db=db,
        session_id=request.session_id,
        mode="pdf",
        role="user",
        message=request.question
    )

    auto_rename_session(db, request.session_id, request.question)
    
    answer = pdf_chat_agent(
        question=request.question,
        user_id=current_user.id,
        session_id=request.session_id
    )
    
    save_message(
        db=db,
        session_id=request.session_id,
        mode="pdf",
        role="assistant",
        message=answer
    )

    return {
        "session_id": request.session_id,
        "response": answer
    }