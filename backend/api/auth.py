from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.dependencies import get_db
from backend.core.security import create_access_token
from backend.schemas.auth_schema import RegisterRequest, LoginRequest, TokenResponse
from backend.services.auth_service import create_user, authenticate_user, get_user_by_email, get_user_by_username

router = APIRouter(tags=["Authentication"])

@router.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):

    if get_user_by_email(db, request.email):
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    if get_user_by_username(db, request.username):
        raise HTTPException(
            status_code=400,
            detail="Username already exists."
        )

    user = create_user(
        db=db,
        username=request.username,
        email=request.email,
        password=request.password
    )
    return {
        "message": "Registration successful.",
        "user_id": user.id
    }

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):

    user = authenticate_user(db, request.email, request.password)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    print("\n========== REGISTER DEBUG ==========")
    print("USERNAME:", request.username)
    print("EMAIL:", request.email)
    print("PASSWORD:", repr(request.password))
    print("====================================")