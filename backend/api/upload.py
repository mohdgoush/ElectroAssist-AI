from pathlib import Path
from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from backend.core.auth import get_current_user
from backend.models.user import User
from backend.services.pdf_services import process_uploaded_pdf

router = APIRouter()

@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):
    save_dir = Path(f"knowledge_base/users/{current_user.id}/uploads")
    save_dir.mkdir(parents=True, exist_ok=True)
    save_path = save_dir / file.filename

    if save_path.exists():
        return {
            "message":
            "PDF already exists in your knowledge base."
        }

    with open(save_path,"wb") as f:
        f.write(await file.read())

    chunks_added = process_uploaded_pdf(
        pdf_path=str(save_path),
        user_id=current_user.id
    )

    return {
        "message":
        f"Successfully indexed '{file.filename}' into your personal knowledge base.",
        "chunks_added": chunks_added
    }