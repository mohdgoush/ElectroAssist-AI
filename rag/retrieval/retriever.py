from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from rag.retrieval.reranker import rerank_documents


# =====================================================
# Embedding Model
# =====================================================

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={
        "device": "cpu"
    }
)


# =====================================================
# Helper
# =====================================================

def load_vectorstore(path: Path):

    if not (path / "index.faiss").exists():
        return None

    return FAISS.load_local(
        str(path),
        embeddings,
        allow_dangerous_deserialization=True
    )


# =====================================================
# Retrieve Context
# =====================================================

def retrieve_context(
    question: str,
    user_id: int,
    retrieval_k: int = 10,
    final_k: int = 4
):

    contexts = []


    # =================================================
    # Developer Knowledge Base
    # =================================================

    developer_store = load_vectorstore(
        Path(
            "knowledge_base/developer/vector_store"
        )
    )

    if developer_store:

        docs = developer_store.similarity_search(
            question,
            k=retrieval_k
        )

        contexts.extend(docs)


    # =================================================
    # User Knowledge Base
    # =================================================

    user_store = load_vectorstore(
        Path(
            f"knowledge_base/users/{user_id}/vector_store"
        )
    )

    if user_store:

        docs = user_store.similarity_search(
            question,
            k=retrieval_k
        )

        contexts.extend(docs)


    # =================================================
    # Remove Duplicate Chunks
    # =================================================

    unique = {}

    for doc in contexts:

        unique[doc.page_content] = doc

    unique_documents = list(
        unique.values()
    )


    # =================================================
    # Rerank Documents
    # =================================================

    reranked_documents = rerank_documents(
        question=question,
        documents=unique_documents,
        top_k=final_k
    )


    # =================================================
    # Build Final Context
    # =================================================

    return "\n\n".join(
        doc.page_content
        for doc in reranked_documents
    )