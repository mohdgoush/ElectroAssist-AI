from typing import TypedDict

class GraphState(TypedDict):
    question: str
    user_id: int
    session_id: int
    route: str
    response: str