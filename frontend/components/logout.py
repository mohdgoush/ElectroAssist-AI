import streamlit as st

from utils.session import logout


def show_logout():

    st.divider()

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        logout()

        st.success(
            "Logged out successfully."
        )

        st.rerun()