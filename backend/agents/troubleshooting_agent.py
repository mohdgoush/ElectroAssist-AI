from backend.services.groq_service import generate_response_with_context
from backend.services.history_service import get_recent_messages

def troubleshooting_agent(question: str, session_id: int):

    history = get_recent_messages(
        session_id=session_id,
        mode="troubleshooting",
        limit=15
    )

    context = f"""
        Conversation History:
        {history}

        Rules:

        1. Diagnose the problem step by step.
        2. Ask ONLY ONE follow-up question if information is missing.
        3. Do NOT provide a long list of possible causes.
        4. Collect enough facts before diagnosing.
        5. Once enough information is available, provide:
        - Root Cause
        - Diagnosis
        - Recommended Fix
        6. Use the conversation history to avoid asking the same question twice.
        7. If the answer already exists in the conversation history, continue from there instead of restarting the troubleshooting process.

        Example:

        User:
        My LED is not glowing.

        Assistant:
        What supply voltage are you using?

        User:
        5V

        Assistant:
        What resistor value are you using?

        User:
        220 ohm

        Assistant:
        Is the long leg of the LED connected to the positive supply?

        Continue the troubleshooting process naturally.
        """
    return generate_response_with_context(question=question, context=context)