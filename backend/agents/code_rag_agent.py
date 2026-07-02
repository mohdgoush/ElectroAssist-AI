from backend.services.code_keyword_extractor import extract_code_keywords
from rag.retrieval.retriever import retrieve_context
from backend.services.groq_service import generate_response_with_context


def code_rag_agent(code: str):

    keywords = extract_code_keywords(code)
    context = retrieve_context(keywords)
    prompt = f"""
        Review this electronics code.

        Code:

        {code}

        Use retrieved datasheet information
        where relevant.
        """
    return generate_response_with_context(prompt, context)