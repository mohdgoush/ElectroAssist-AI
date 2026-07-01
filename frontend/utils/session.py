import streamlit as st

def set_token(token):
    st.session_state.token = token


def set_logged_in(flag):
    st.session_state.logged_in = flag


def set_user_email(email):
    st.session_state.user_email = email


def set_username(username):
    st.session_state.username = username
# =====================================================
# Initialize Session State
# =====================================================

def initialize_session():

    defaults = {

        # -----------------------------
        # Authentication
        # -----------------------------
        "logged_in": False,
        "token": None,
        "user_email": None,

        # -----------------------------
        # User Information
        # -----------------------------
        "username": None,

        # -----------------------------
        # Chat
        # -----------------------------
        "messages": [],

        # -----------------------------
        # Current Working Mode
        # -----------------------------
        "current_mode": "text",

        # -----------------------------
        # PDF
        # -----------------------------
        "current_pdf": None,

        # -----------------------------
        # Circuit
        # -----------------------------
        "current_circuit_analysis": None,

        # -----------------------------
        # Upload Tracking
        # -----------------------------
        "last_uploaded_file": None,

        # -----------------------------
        # Chat Sessions
        # (For Future Use)
        # -----------------------------
        "current_session_id": None,
        "current_session_name": "New Chat",

        # -----------------------------
        # Cached Session List
        # (Future Sidebar)
        # -----------------------------
        "sessions": []
    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


# =====================================================
# Clear Current Chat
# =====================================================

def clear_chat():

    st.session_state.messages = []

    st.session_state.current_mode = "text"

    st.session_state.current_pdf = None

    st.session_state.current_circuit_analysis = None

    st.session_state.last_uploaded_file = None

    st.session_state.current_session_id = None

    st.session_state.current_session_name = "New Chat"


# =====================================================
# Logout
# =====================================================

def logout():

    keys = [

        "logged_in",
        "token",
        "user_email",
        "username",

        "messages",

        "current_mode",
        "current_pdf",
        "current_circuit_analysis",
        "last_uploaded_file",

        "current_session_id",
        "current_session_name",
        "sessions"
    ]

    for key in keys:

        if key in st.session_state:

            del st.session_state[key]

    initialize_session()


# =====================================================
# Authentication Helpers
# =====================================================

def is_logged_in():

    return st.session_state.logged_in


def get_token():

    return st.session_state.token


def get_username():

    return st.session_state.username


def get_user_email():

    return st.session_state.user_email


# =====================================================
# Chat Helpers
# =====================================================

def add_user_message(message):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": message
        }
    )


def add_assistant_message(message):

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": message
        }
    )


def get_messages():

    return st.session_state.messages


# =====================================================
# Mode Helpers
# =====================================================

def set_mode(mode):

    st.session_state.current_mode = mode


def get_mode():

    return st.session_state.current_mode


# =====================================================
# PDF Helpers
# =====================================================

def set_current_pdf(filename):

    st.session_state.current_pdf = filename


def get_current_pdf():

    return st.session_state.current_pdf


# =====================================================
# Circuit Helpers
# =====================================================

def set_circuit_analysis(analysis):

    st.session_state.current_circuit_analysis = analysis


def get_circuit_analysis():

    return st.session_state.current_circuit_analysis


# =====================================================
# Upload Helpers
# =====================================================

def set_last_uploaded_file(filename):

    st.session_state.last_uploaded_file = filename


def get_last_uploaded_file():

    return st.session_state.last_uploaded_file


# =====================================================
# Future Session Helpers
# =====================================================

def set_current_session(session_id, session_name):

    st.session_state.current_session_id = session_id

    st.session_state.current_session_name = session_name


def get_current_session():

    return (
        st.session_state.current_session_id,
        st.session_state.current_session_name
    )
def clear_pdf():

    st.session_state.current_pdf = None


def clear_circuit():

    st.session_state.current_circuit_analysis = None


def reset_upload_state():

    clear_pdf()

    clear_circuit()

    st.session_state.last_uploaded_file = None

    st.session_state.current_mode = "text"

# =====================================================
# Session List Helpers
# =====================================================

def set_sessions(sessions):

    st.session_state.sessions = sessions


def get_sessions():

    return st.session_state.sessions


def set_current_session(session_id, session_name):

    st.session_state.current_session_id = session_id
    st.session_state.current_session_name = session_name


def get_current_session():

    return (
        st.session_state.current_session_id,
        st.session_state.current_session_name
    )