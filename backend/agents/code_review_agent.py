from backend.services.groq_service import (
    generate_response_with_context
)

from backend.services.history_service import (
    get_recent_messages
)


def code_review_agent(
    message: str,
    session_id: int
):

    history = get_recent_messages(
    session_id=session_id,
    mode="code",
    limit=15
)

    context = f"""
Conversation History:
{history}

The user may provide:

- Arduino code
- ESP32 code
- STM32 code
- Verilog
- VHDL

Determine the user's intent before answering.

Possible intents:

1. Syntax Fix
2. Debug Code
3. Explain Code
4. Code Review
5. Optimize Code

--------------------------------------------------

If intent = Syntax Fix

Return:

CORRECTED CODE:
<corrected code>

SYNTAX ERRORS:
- error 1
- error 2

--------------------------------------------------

If intent = Debug Code

Return:

BUG FOUND:
...

CAUSE:
...

FIX:
...

--------------------------------------------------

If intent = Explain Code

Return:

SUMMARY:
...

LINE-BY-LINE EXPLANATION:
...

--------------------------------------------------

If intent = Optimize Code

Return:

OPTIMIZED CODE:
...

WHY IT IS BETTER:
...

--------------------------------------------------

If intent = Code Review

Return:

CODE SUMMARY:
...

BUGS / ERRORS:
...

IMPROVEMENTS:
...

BEST PRACTICES:
...

Important Rules:

- Use the conversation history to understand follow-up questions.
- If the user asks a follow-up question about previously shared code,
  continue reviewing that same code instead of asking them to paste it again.
- For Verilog/VHDL, do NOT mention microcontrollers.
- Do NOT invent hardware.
- Focus only on the provided code.
- If the code is incomplete, explain what is missing.
- If the user asks ONLY for syntax correction, do NOT perform a full code review.
- Preserve the programming language used by the user.

If the user asks a follow-up question such as:

"Optimize it"

"Explain line 5"

"Fix only the syntax"

continue using the previously shared code from the conversation history.
"""

    return generate_response_with_context(
        question=message,
        context=context
    )