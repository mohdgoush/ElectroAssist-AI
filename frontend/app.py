import streamlit as st

from utils.session import (
    initialize_session,
    is_logged_in
)

from components.login import (
    show_login_page
)

from components.sidebar import (
    show_sidebar
)

from components.uploader import (
    process_upload
)

from components.examples import (
    show_examples
)

from components.chat import (
    show_chat
)

from services.session_manager import (
    load_sessions,
    create_new_session
)

from utils.session import (
    get_current_session
)

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="⚡ ElectroAssist AI",
    page_icon="⚡",
    layout="wide"
)

# =====================================================
# Initialize Session
# =====================================================

initialize_session()

# =====================================================
# Authentication
# =====================================================

if not is_logged_in():

    show_login_page()

    st.stop()

# =====================================================
# Auto Create First Chat
# =====================================================

sessions = load_sessions()

current_session_id, _ = get_current_session()

if current_session_id is None:

    if len(sessions) == 0:

        create_new_session()

    else:

        first = sessions[0]

        from services.session_manager import load_session

        load_session(
            first["id"],
            first["session_name"]
        )

    st.rerun()
# =====================================================
# Main Header
# =====================================================

st.title("⚡ ElectroAssist AI")

st.caption(
    "Intelligent Electronics Engineering Assistant"
)

# =====================================================
# Sidebar
# =====================================================

uploaded_file = show_sidebar()

# =====================================================
# Upload Processing
# =====================================================

process_upload(uploaded_file)

# =====================================================
# Example Questions
# =====================================================

show_examples()

# =====================================================
# Chat Interface
# =====================================================

show_chat()