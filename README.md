# ⚡ ElectroAssist AI

> **A Multi-Agent AI Assistant for Electronics Engineering powered by
> LangGraph, FastAPI, Retrieval-Augmented Generation (RAG), and Vision
> AI.**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-orange)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

------------------------------------------------------------------------

## 📖 Overview

ElectroAssist AI is an intelligent assistant built for electronics
students, engineers, and embedded developers. It combines Large Language
Models, Retrieval-Augmented Generation (RAG), Computer Vision, and
LangGraph-based multi-agent orchestration.

### Features

-   JWT Authentication
-   Multi-user support
-   Multi-session chat
-   LangGraph multi-agent routing
-   PDF Chat (RAG)
-   Personal knowledge base
-   User-isolated FAISS vector stores
-   Circuit image analysis
-   Verilog/VHDL code review
-   Electronics troubleshooting
-   Streaming AI responses
-   PostgreSQL chat history

## 🏗️ System Architecture

``` mermaid
flowchart TB
User([User]) --> Streamlit
Streamlit --> FastAPI
FastAPI --> LangGraph
LangGraph --> Knowledge
LangGraph --> PDF
LangGraph --> Circuit
LangGraph --> Code
LangGraph --> Troubleshooting

Knowledge --> FAISS
PDF --> FAISS
Circuit --> Gemini

FAISS --> DeveloperKB[(Developer KB)]
FAISS --> UserKB[(User KB)]

Knowledge --> Groq
PDF --> Groq
Code --> Groq
Troubleshooting --> Groq

FastAPI --> PostgreSQL[(PostgreSQL)]
```

## 🛠 Tech Stack

-   Python
-   FastAPI
-   Streamlit
-   LangGraph
-   LangChain
-   Groq
-   Google Gemini
-   FAISS
-   HuggingFace Embeddings
-   PostgreSQL
-   SQLAlchemy

## 📂 Project Structure

``` text
ElectroAssist-AI/
├── backend/
├── frontend/
├── knowledge_base/
├── rag/
├── requirements.txt
└── README.md
```

## ⚙️ Installation

``` bash
git clone https://github.com/<your-username>/ElectroAssist-AI.git
cd ElectroAssist-AI

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

## 🔑 Environment Variables

``` env
DATABASE_URL=
SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080
GROQ_API_KEY=
GEMINI_API_KEY=
```

## ▶️ Run

Backend:

``` bash
uvicorn backend.main:app --reload
```

Frontend:

``` bash
streamlit run frontend/app.py
```

## 🚀 Future Improvements

-   Voice Assistant
-   OCR Improvements
-   Cloud Storage
-   Web Search
-   Multi-modal RAG
-   Team Workspaces

## 📄 License

MIT License

## 👨‍💻 Author

**Mohd Goush**

B.Tech Electronics & Communication Engineering\
Institute of Engineering & Technology (IET), Lucknow
