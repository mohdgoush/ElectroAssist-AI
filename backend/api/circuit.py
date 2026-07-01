from pathlib import Path

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from backend.agents.circuit_agent import (
    circuit_agent
)
from fastapi import Depends

from backend.core.auth import get_current_user
from backend.models.user import User

router = APIRouter()


@router.post("/analyze-circuit")

async def analyze_circuit(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):

    save_dir = Path(
        "uploads/images"
    )

    save_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    save_path = (
        save_dir / file.filename
    )

    with open(
        save_path,
        "wb"
    ) as f:

        f.write(
            await file.read()
        )

    result = circuit_agent(
    image_path=str(save_path),
    user_id=current_user.id
)

    return {
        "analysis": result
    }