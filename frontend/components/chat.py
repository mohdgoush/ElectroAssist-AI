import streamlit as st
import requests
import time
from api import send_chat_message, ask_pdf, ask_circuit, parse_response
from utils.session import get_messages, add_user_message,add_assistant_message,get_mode,get_token,get_circuit_analysis,get_current_session


def show_chat():

    for message in get_messages():
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input(
        "Ask anything about Electronics..."
    )

    if not prompt:
        return

    session_id, _ = get_current_session()
    if session_id is None:
        st.warning("Please create a new chat first.")
        return

    add_user_message(prompt)
    with st.chat_message("user"):
        st.markdown(prompt)

    answer = ""

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                token = get_token()
                mode = get_mode()
                if mode == "text":
                    response = send_chat_message(session_id,prompt,token)

                elif mode == "pdf":
                    response = ask_pdf(session_id, prompt, token)

                elif mode == "circuit":
                    response = ask_circuit(session_id,prompt,get_circuit_analysis(),token)
                else:

                    response = send_chat_message(session_id,prompt,token)

                answer = parse_response(response)
            except requests.exceptions.ConnectionError:
                answer = "❌ Backend is not running."
            except requests.exceptions.Timeout:

                answer = "⏳ Backend timeout."

            except Exception as e:
                answer = str(e)

        placeholder = st.empty()
        streamed = ""

        for char in answer:
            streamed += char
            placeholder.markdown(streamed + "▌")
            time.sleep(0.006)

        placeholder.markdown(streamed)
        add_assistant_message(streamed)