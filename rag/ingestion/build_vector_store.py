from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


KNOWLEDGE_BASE_PATH = "knowledge_base"
VECTOR_DB_PATH = "rag/vector_store/faiss_index"


def load_documents():

    documents = []

    pdf_files = list(
        Path(KNOWLEDGE_BASE_PATH).rglob("*.pdf")
    )

    print(f"\nFound {len(pdf_files)} PDFs\n")

    for pdf in pdf_files:

        print(f"Loading: {pdf}")

        try:

            loader = PyPDFLoader(str(pdf))

            documents.extend(
                loader.load()
            )

        except Exception as e:

            print(
                f"Error loading {pdf}: {e}"
            )

    return documents


def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(
        documents
    )

    return chunks


def create_vector_db(chunks):

    print("\nLoading embedding model...\n")

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={
            "device": "cpu"
        }
    )

    print(
        "\nEmbedding model loaded successfully"
    )

    print(
        "\nGenerating embeddings and creating FAISS index..."
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    print(
        "\nSaving vector database..."
    )

    vectorstore.save_local(
        VECTOR_DB_PATH
    )

    print(
        f"\nVector DB saved to: {VECTOR_DB_PATH}"
    )


if __name__ == "__main__":

    print(
        "\n========== ELECTROASSIST VECTOR DB BUILDER ==========\n"
    )

    print(
        "Loading documents...\n"
    )

    documents = load_documents()

    print(
        f"\nLoaded {len(documents)} pages"
    )

    print(
        "\nCreating chunks...\n"
    )

    chunks = create_chunks(
        documents
    )

    print(
        f"\nCreated {len(chunks)} chunks"
    )

    create_vector_db(
        chunks
    )

    print(
        "\n========== VECTOR DATABASE CREATED SUCCESSFULLY ==========\n"
    )