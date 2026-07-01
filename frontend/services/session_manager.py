import streamlit as st

from api import (
    create_session,
    get_sessions,
    get_session_messages,
    delete_session,
    parse_response,
    clear_current_chat,
    clear_all_chats
)

from utils.session import (
    get_token,
    set_sessions,
    get_sessions as get_cached_sessions,
    set_current_session,
    clear_chat,
    add_user_message,
    add_assistant_message,
    get_current_session
)


# =====================================================
# Load User Sessions
# =====================================================

def load_sessions():

    token = get_token()

    response = get_sessions(token)

    if response.status_code == 200:

        sessions = response.json()

        set_sessions(sessions)

        return sessions

    return get_cached_sessions()


# =====================================================
# Create New Session
# =====================================================

def create_new_session():

    token = get_token()

    response = create_session(
        "New Chat",
        token
    )

    if response.status_code != 200:

        st.error(
            parse_response(response)
        )

        return None

    session = response.json()

    set_current_session(
        session["id"],
        session["session_name"]
    )

    clear_chat()

    load_sessions()

    return session


# =====================================================
# Load One Session
# =====================================================

def load_session(session_id, session_name):

    token = get_token()

    clear_chat()

    set_current_session(
        session_id,
        session_name
    )

    response = get_session_messages(
        session_id,
        token
    )

    if response.status_code != 200:

        st.error(
            parse_response(response)
        )

        return

    messages = response.json()

    for message in messages:

        if message["role"] == "user":

            add_user_message(
                message["message"]
            )

        else:

            add_assistant_message(
                message["message"]
            )


# =====================================================
# Delete Session
# =====================================================

def remove_session(session_id):

    token = get_token()

    response = delete_session(
        session_id,
        token
    )

    if response.status_code != 200:

        st.error(
            parse_response(response)
        )

        return

    clear_chat()

    load_sessions()
# =====================================================
# Clear Current Chat
# =====================================================

def clear_current_session():

    token = get_token()

    session_id, _ = get_current_session()

    response = clear_current_chat(
        session_id,
        token
    )

    if response.status_code != 200:

        st.error(
            parse_response(response)
        )

        return

    clear_chat()

# =====================================================
# Clear All Chats
# =====================================================

def remove_all_sessions():

    token = get_token()

    response = clear_all_chats(
        token
    )

    if response.status_code != 200:

        st.error(
            parse_response(response)
        )

        return

    clear_chat()

    set_sessions([])

    set_current_session(None, None)