import streamlit as st

from services.session_manager import (
    create_new_session,
    load_sessions,
    load_session,
    clear_current_session,
    remove_all_sessions
)

from utils.session import (
    get_username,
    get_user_email,
    clear_chat,
    get_mode,
    get_current_pdf,
    get_current_session
)

from components.logout import show_logout


def show_sidebar():

    with st.sidebar:

        # =====================================================
        # Header
        # =====================================================

        st.header("⚡ ElectroAssist AI")

        username = get_username()

        if username:

            st.success(f"👤 {username}")

        else:

            st.success(get_user_email())

        st.divider()

        # =====================================================
        # New Chat
        # =====================================================

        if st.button(
            "➕ New Chat",
            use_container_width=True
        ):

            create_new_session()

            st.rerun()

        st.divider()

        # =====================================================
        # Chats
        # =====================================================

        st.subheader("💬 Chats")

        sessions = load_sessions()

        current_session_id, _ = get_current_session()

        if len(sessions) == 0:

            st.info(
                "No chats yet."
            )

        else:

            for session in sessions:

                label = session["session_name"]

                if session["id"] == current_session_id:

                    label = "🟢 " + label

                if st.button(
                    label,
                    key=f"chat_{session['id']}",
                    use_container_width=True
                ):

                    load_session(
                        session["id"],
                        session["session_name"]
                    )

                    st.rerun()

        st.divider()

        # =====================================================
        # Clear Current Chat
        # =====================================================
        st.subheader("🗂 Chat Management")
        if st.button(
            "🧹 Clear Current Chat",
            use_container_width=True
        ):

            clear_current_session()

            st.success(
                "Current chat cleared."
            )

            st.rerun()
        
        # -----------------------------
        # Clear All Chats
        # -----------------------------

        if st.button(
            "🗑 Clear All Chats",
            use_container_width=True
        ):

            remove_all_sessions()

            st.success(
                "All chats deleted."
            )

            st.rerun()

        st.divider()

        # =====================================================
        # Upload
        # =====================================================

        st.subheader("📎 Upload")

        uploaded_file = st.file_uploader(
            "Upload PDF or Circuit",
            type=[
                "pdf",
                "png",
                "jpg",
                "jpeg"
            ],
            label_visibility="collapsed"
        )

        st.divider()

        # =====================================================
        # Current Session
        # =====================================================

        st.subheader("📋 Current Session")

        mode = get_mode()

        mode_map = {
            "text": "💬 General Chat",
            "pdf": "📄 PDF Chat",
            "circuit": "🔌 Circuit Analysis",
            "code": "💻 Code Review"
        }

        st.write(
            mode_map.get(
                mode,
                mode
            )
        )

        pdf = get_current_pdf()

        if pdf:

            st.caption(
                f"📄 {pdf}"
            )

        st.divider()

        # =====================================================
        # Logout
        # =====================================================

        show_logout()

        return uploaded_file