from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


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
    k: int = 4
):

    contexts = []

    # ----------------------------------------
    # Developer Knowledge Base
    # ----------------------------------------

    developer_store = load_vectorstore(
        Path("knowledge_base/developer/vector_store")
    )

    if developer_store:

        docs = developer_store.similarity_search(
            question,
            k=k
        )

        contexts.extend(docs)

    # ----------------------------------------
    # User Knowledge Base
    # ----------------------------------------

    user_store = load_vectorstore(
        Path(
            f"knowledge_base/users/{user_id}/vector_store"
        )
    )

    if user_store:

        docs = user_store.similarity_search(
            question,
            k=k
        )

        contexts.extend(docs)

    # ----------------------------------------
    # Remove Duplicate Chunks
    # ----------------------------------------

    unique = {}

    for doc in contexts:

        unique[doc.page_content] = doc

    return "\n\n".join(
        doc.page_content
        for doc in unique.values()
    )