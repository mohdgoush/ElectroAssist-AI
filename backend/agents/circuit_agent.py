from backend.agents.vision_rag_agent import (
    vision_rag_agent
)


def circuit_agent(
    image_path,
    user_id
):

    return vision_rag_agent(
        image_path=image_path,
        user_id=user_id
    )