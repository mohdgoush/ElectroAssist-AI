from backend.services.groq_service import (
    generate_response_with_context
)

from backend.services.history_service import (
    get_recent_messages
)

from rag.retrieval.retriever import (
    retrieve_context
)


def pdf_chat_agent(
    question: str,
    user_id: int,
    session_id: int
):

    history = get_recent_messages(
        session_id=session_id,
        mode="pdf",
        limit=15
    )

    context = retrieve_context(
        question=question,
        user_id=user_id
    )

    full_context = f"""
Conversation History:
{history}

The user has uploaded one or more PDF documents.

Relevant Context:

{context}
"""

    return generate_response_with_context(
        question=question,
        context=full_context
    )