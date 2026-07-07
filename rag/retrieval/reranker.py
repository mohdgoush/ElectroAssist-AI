from sentence_transformers import CrossEncoder

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")
def rerank_documents(question: str, documents: list, top_k: int = 4):

    if not documents:
        return []

    pairs = [
        (question, doc.page_content)
        for doc in documents
    ]

    scores = reranker.predict(pairs)
    scored_documents = list(zip(documents, scores))

    scored_documents.sort(key=lambda item: item[1],reverse=True)

    return [document for document, score in scored_documents[:top_k]]