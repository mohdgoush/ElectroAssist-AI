import streamlit as st

from api import (
    upload_pdf,
    analyze_circuit,
    parse_response
)

from utils.session import (
    get_token,
    set_mode,
    set_current_pdf,
    set_circuit_analysis,
    set_last_uploaded_file,
    get_last_uploaded_file,
    add_assistant_message,
    clear_pdf,
    clear_circuit
)


def process_upload(uploaded_file):

    if uploaded_file is None:
        return

    if uploaded_file.name == get_last_uploaded_file():
        return

    token = get_token()

    # =====================================================
    # PDF Upload
    # =====================================================

    if uploaded_file.type == "application/pdf":

        clear_circuit()

        with st.spinner("Processing PDF..."):

            response = upload_pdf(
                uploaded_file,
                token
            )

            if response.status_code != 200:

                st.error(
                    parse_response(response)
                )
                return

            set_mode("pdf")

            set_current_pdf(
                uploaded_file.name
            )

            set_last_uploaded_file(
                uploaded_file.name
            )

            add_assistant_message(
                f"📄 **{uploaded_file.name}** uploaded successfully.\n\n"
                "Ask me anything about this PDF."
            )

            st.rerun()

    # =====================================================
    # Circuit Upload
    # =====================================================

    elif uploaded_file.type.startswith("image"):

        clear_pdf()

        with st.spinner("Analyzing Circuit..."):

            response = analyze_circuit(
                uploaded_file,
                token
            )

            if response.status_code != 200:

                st.error(
                    parse_response(response)
                )
                return

            analysis = response.json()["analysis"]

            set_mode("circuit")

            set_circuit_analysis(
                analysis
            )

            set_last_uploaded_file(
                uploaded_file.name
            )

            add_assistant_message(
                "🔌 Circuit analyzed successfully.\n\n"
                "Ask me anything about this circuit."
            )

            st.rerun()

    # =====================================================
    # Unsupported File
    # =====================================================

    else:

        st.error(
            "Unsupported file type."
        )