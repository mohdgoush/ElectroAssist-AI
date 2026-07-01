from backend.services.groq_service import (
    generate_response_with_context
)

from backend.services.history_service import (
    get_recent_messages
)


def circuit_chat_agent(
    question: str,
    analysis: str,
    session_id: int
):

    history = get_recent_messages(
        session_id=session_id,
        mode="circuit",
        limit=15
    )

    context = f"""
Conversation History:
{history}

The user has already uploaded a circuit image.

The image has already been analyzed.

Use ONLY the following analysis of that uploaded image when answering.

Circuit Analysis:

{analysis}
"""

    return generate_response_with_context(
        question=question,
        context=context
    )