from fastapi import FastAPI
from backend.core.database import engine
from backend.models.base import Base
from fastapi import APIRouter, Depends
# Import all models
from backend.api.chat import router as chat_router
from backend.api.history import router as history_router
from backend.api.upload import router as upload_router
from backend.api.circuit import router as circuit_router
from backend.api.code_review import router as code_router
from backend.api.pdf_chat import router as pdf_chat_router
from backend.api.circuit_chat import router as circuit_chat_router
from backend.models.user import User
from backend.models.session import Session
from backend.models.chat_history import ChatHistory
from backend.api.auth import router as auth_router
from backend.core.auth import get_current_user
from backend.api.me import router as me_router
from backend.api.session import router as session_router

Base.metadata.create_all(bind=engine)
router = APIRouter()
app = FastAPI(
    title="ElectroAssist AI",
    version="1.0.0"
)



app.include_router(history_router)
app.include_router(chat_router)
app.include_router(upload_router)
app.include_router(circuit_router)
app.include_router(code_router)
app.include_router(pdf_chat_router)
app.include_router(circuit_chat_router)
app.include_router(auth_router)
app.include_router(me_router)
app.include_router(session_router)

@app.get("/")
def home():
    return {
        "message": "ElectroAssist AI Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
