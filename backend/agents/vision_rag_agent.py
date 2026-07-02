from backend.services.gemini_service import analyze_circuit_image
from backend.services.component_extractor import extract_components
from rag.retrieval.retriever import retrieve_context
from backend.services.groq_service import generate_response_with_context

def vision_rag_agent(image_path, user_id):

    vision_result = analyze_circuit_image(image_path)
    components = extract_components(vision_result)
    search_query = " ".join(components)
    context = retrieve_context(
        question=search_query,
        user_id=user_id
    )

    prompt = f"""
        You are an Electronics Expert.

        Vision Analysis:
        {vision_result}

        Knowledge Base Context:
        {context}

        Provide:

        1. Components
        2. Circuit Purpose
        3. Fault Analysis
        4. Troubleshooting Steps
        5. Relevant Datasheet Knowledge
        """
    final_answer = generate_response_with_context(
        question="Analyze this circuit.",
        context=prompt
    )
    return final_answer