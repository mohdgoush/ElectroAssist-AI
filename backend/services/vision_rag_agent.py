from backend.services.gemini_service import analyze_circuit_image
from backend.services.component_extractor import extract_components
from rag.retrieval.retriever import retrieve_context
from backend.services.groq_service import generate_response_with_context
from backend.services.vision_parser import parse_vision_response

def vision_rag_agent(image_path: str):

    vision_result = analyze_circuit_image(image_path)
    vision_data = parse_vision_response(vision_result)
    components = vision_data["components"]
    search_query = f"""Components:{' '.join(components)}
        Circuit:
        {vision_data['circuit_type']}
        """
    rag_context = retrieve_context(search_query)
    combined_context = f"""
        Analyze this circuit.

        Detected Components:
        {', '.join(components)}

        Circuit Type:
        {vision_data['circuit_type']}

        Detected Issues:
        {', '.join(vision_data['possible_issues'])}

        Use the retrieved knowledge base information
        to provide:

        1. Circuit Purpose
        2. Component Functions
        3. Fault Analysis
        4. Troubleshooting Steps
        5. Relevant Datasheet Information
        """

    final_answer = generate_response_with_context(question="Analyze this circuit.", context=combined_context)
    return final_answer