from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"}
)


def retrieve_uploaded_context(query):

    vectorstore = FAISS.load_local(
        "uploads/temp_faiss",
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = vectorstore.similarity_search(
        query,
        k=4
    )

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )