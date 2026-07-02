from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"}
)

def process_uploaded_pdf(pdf_path: str, user_id: int):

    vector_db_path = Path(f"knowledge_base/users/{user_id}/vector_store")
    vector_db_path.mkdir(parents=True,exist_ok=True)
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)
    faiss_index = vector_db_path / "index.faiss"

    if faiss_index.exists():
        vectorstore = FAISS.load_local(str(vector_db_path), embeddings, allow_dangerous_deserialization=True)
        vectorstore.add_documents(chunks)
    else:
        vectorstore = FAISS.from_documents(chunks, embeddings)

    vectorstore.save_local(str(vector_db_path))
    return len(chunks)