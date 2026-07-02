from fastapi import APIRouter, Depends

from backend.core.auth import get_current_user
from backend.models.user import User

router = APIRouter(tags=["Authentication"])


@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }