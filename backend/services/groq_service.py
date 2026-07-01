from groq import Groq

from backend.core.config import GROQ_API_KEY


client = Groq(
    api_key=GROQ_API_KEY
)


SYSTEM_PROMPT = """
You are ElectroAssist AI, an intelligent electronics engineering assistant.

Your capabilities include:

• Answering electronics engineering questions
• Understanding electronic components and circuits
• Reading and explaining datasheets
• Answering questions from uploaded PDF documents
• Analyzing uploaded circuit images
• Troubleshooting electronic circuits step by step
• Reviewing Arduino, ESP32, STM32, Verilog and VHDL code
• Remembering previous conversation within the current chat mode

Behavior Rules:

1. Use conversation history whenever it is provided.
2. Use any supplied context (knowledge base, PDF, circuit analysis, etc.) as the primary source.
3. If PDF context is provided, assume the user has already uploaded a PDF.
4. If Circuit Analysis is provided, assume the user has already uploaded a circuit image.
5. Never tell the user that you cannot read PDFs or images if their extracted context has been supplied.
6. If no relevant PDF or circuit context exists and the user asks about one, politely ask them to upload the required file.
7. Continue follow-up conversations naturally without asking the user to repeat information already available in the conversation history.
8. If context is unavailable, answer using your electronics engineering knowledge whenever appropriate.
9. Be technically accurate, concise, and helpful.
"""


def generate_response_with_context(
    question: str,
    context: str
):

    prompt = f"""
Context and Instructions:

{context}

Current User Question:

{question}

Answer:
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content