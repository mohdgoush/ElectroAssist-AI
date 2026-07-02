from backend.agents.vision_rag_agent import vision_rag_agent

def circuit_agent(image_path: str):
    return vision_rag_agent(image_path)