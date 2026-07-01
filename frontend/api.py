import requests

from config import (
    LOGIN_URL,
    REGISTER_URL,
    ME_URL,
    CREATE_SESSION_URL,
    GET_SESSIONS_URL,
    SESSION_HISTORY_URL,
    CHAT_URL,
    UPLOAD_URL,
    PDF_CHAT_URL,
    CIRCUIT_ANALYSIS_URL,
    CIRCUIT_CHAT_URL,
    CODE_REVIEW_URL,
    CLEAR_CHAT_URL,
    CLEAR_ALL_CHATS_URL
)


# =====================================================
# Common Headers
# =====================================================

def get_headers(token=None):

    headers = {}

    if token:

        headers["Authorization"] = f"Bearer {token}"

    return headers


# =====================================================
# Authentication APIs
# =====================================================

def register(
    username: str,
    email: str,
    password: str
):

    return requests.post(
        REGISTER_URL,
        json={
            "username": username,
            "email": email,
            "password": password
        },
        timeout=60
    )


def login(
    email: str,
    password: str
):

    return requests.post(
        LOGIN_URL,
        json={
            "email": email,
            "password": password
        },
        timeout=60
    )


def get_current_user(token):

    return requests.get(
        ME_URL,
        headers=get_headers(token),
        timeout=60
    )

# =====================================================
# Sessions
# =====================================================

def create_session(
    session_name,
    token
):

    return requests.post(
        CREATE_SESSION_URL,
        json={
            "session_name": session_name
        },
        headers=get_headers(token),
        timeout=60
    )


def get_sessions(
    token
):

    return requests.get(
        GET_SESSIONS_URL,
        headers=get_headers(token),
        timeout=60
    )


def delete_session(
    session_id,
    token
):

    return requests.delete(
        f"{GET_SESSIONS_URL}/{session_id}",
        headers=get_headers(token),
        timeout=60
    )


def get_session_messages(
    session_id,
    token
):

    return requests.get(
        f"{SESSION_HISTORY_URL}/{session_id}/messages",
        headers=get_headers(token),
        timeout=60
    )
# =====================================================
# Sessions
# =====================================================

def create_session(
    session_name,
    token
):

    return requests.post(
        CREATE_SESSION_URL,
        json={
            "session_name": session_name
        },
        headers=get_headers(token),
        timeout=60
    )


def get_sessions(
    token
):

    return requests.get(
        GET_SESSIONS_URL,
        headers=get_headers(token),
        timeout=60
    )


def delete_session(
    session_id,
    token
):

    return requests.delete(
        f"{GET_SESSIONS_URL}/{session_id}",
        headers=get_headers(token),
        timeout=60
    )


def get_session_messages(
    session_id,
    token
):

    return requests.get(
        f"{SESSION_HISTORY_URL}/{session_id}/messages",
        headers=get_headers(token),
        timeout=60
    )
# =====================================================
# General Chat
# =====================================================

def send_chat_message(
    session_id,
    message,
    token
):

    return requests.post(
        CHAT_URL,
        json={
            "session_id": session_id,
            "message": message
        },
        headers=get_headers(token),
        timeout=60
    )


# =====================================================
# PDF Upload
# =====================================================

def upload_pdf(
    uploaded_file,
    token
):

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    return requests.post(
        UPLOAD_URL,
        files=files,
        headers=get_headers(token),
        timeout=60
    )


# =====================================================
# PDF Chat
# =====================================================

def ask_pdf(
    session_id,
    question,
    token
):

    return requests.post(
        PDF_CHAT_URL,
        json={
            "session_id": session_id,
            "question": question
        },
        headers=get_headers(token),
        timeout=60
    )


# =====================================================
# Circuit Upload
# =====================================================

def analyze_circuit(
    uploaded_file,
    token
):

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    return requests.post(
        CIRCUIT_ANALYSIS_URL,
        files=files,
        headers=get_headers(token),
        timeout=60
    )


# =====================================================
# Circuit Chat
# =====================================================

def ask_circuit(
    session_id,
    question,
    analysis,
    token
):

    return requests.post(
        CIRCUIT_CHAT_URL,
        json={
            "session_id": session_id,
            "question": question,
            "analysis": analysis
        },
        headers=get_headers(token),
        timeout=60
    )


# =====================================================
# Code Review
# =====================================================

def review_code(
    session_id,
    message,
    token
):

    return requests.post(
        CODE_REVIEW_URL,
        json={
            "session_id": session_id,
            "message": message
        },
        headers=get_headers(token),
        timeout=60
    )


# =====================================================
# Helper
# =====================================================

def parse_response(response):

    if response.status_code == 200:

        data = response.json()

        return (
            data.get("response")
            or data.get("review")
            or data.get("analysis")
            or data.get("message")
            or "No response received."
        )

    try:

        data = response.json()

        message = (
            data.get("detail")
            or data.get("message")
            or response.text
        )

    except Exception:

        message = response.text

    return (
        f"❌ Backend Error ({response.status_code})\n\n"
        f"{message}"
    )

# =====================================================
# Clear Current Chat
# =====================================================

def clear_current_chat(
    session_id,
    token
):

    return requests.delete(
        f"{CLEAR_CHAT_URL}/{session_id}/messages",
        headers=get_headers(token),
        timeout=60
    )


# =====================================================
# Clear All Chats
# =====================================================

def clear_all_chats(
    token
):

    return requests.delete(
        CLEAR_ALL_CHATS_URL,
        headers=get_headers(token),
        timeout=60
    )