from backend.core.database import SessionLocal
from backend.models.chat_history import ChatHistory


def get_recent_messages(
    session_id: int,
    mode: str,
    limit: int = 10
):

    db = SessionLocal()

    try:

        messages = (
            db.query(ChatHistory)
            .filter(
                ChatHistory.session_id == session_id,
                ChatHistory.mode == mode
            )
            .order_by(ChatHistory.id.desc())
            .limit(limit)
            .all()
        )

        messages.reverse()

        return "\n".join(
            f"{msg.role}: {msg.message}"
            for msg in messages
        )

    finally:
        db.close()