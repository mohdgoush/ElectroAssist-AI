import streamlit as st

from api import (
    login,
    register,
    get_current_user,
    parse_response
)

from utils.session import (
    set_logged_in,
    set_token,
    set_user_email,
    set_username
)


def show_login_page():

    st.title("⚡ ElectroAssist AI")

    st.caption(
        "AI Powered Electronics Engineering Assistant"
    )

    tab1, tab2 = st.tabs(
        [
            "🔑 Login",
            "📝 Register"
        ]
    )

    # =====================================================
    # LOGIN
    # =====================================================

    with tab1:

        st.subheader("Login")

        email = st.text_input(
            "Email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button(
            "Login",
            use_container_width=True
        ):

            if not email or not password:

                st.warning(
                    "Please enter both email and password."
                )

                return

            response = login(
                email,
                password
            )

            if response.status_code != 200:

                st.error(
                    parse_response(response)
                )

                return

            data = response.json()

            token = data["access_token"]

            user_response = get_current_user(
                token
            )

            if user_response.status_code != 200:

                st.error(
                    parse_response(user_response)
                )

                return

            user_data = user_response.json()

            set_logged_in(True)

            set_token(token)

            set_user_email(
                user_data["email"]
            )

            set_username(
                user_data["username"]
            )

            st.success(
                f"Welcome, {user_data['username']}!"
            )

            st.rerun()

    # =====================================================
    # REGISTER
    # =====================================================

    with tab2:

        st.subheader(
            "Create Account"
        )

        username = st.text_input(
            "Username",
            key="register_username"
        )

        email = st.text_input(
            "Email",
            key="register_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="register_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            key="register_confirm_password"
        )

        if st.button(
            "Register",
            use_container_width=True
        ):

            if not username or not email or not password:

                st.warning(
                    "Please fill in all fields."
                )

                return

            if password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

                return

            response = register(
                username,
                email,
                password
            )

            if response.status_code == 200:

                st.success(
                    "✅ Registration successful!\n\nPlease login using your new account."
                )

            else:

                st.error(
                    parse_response(response)
                )