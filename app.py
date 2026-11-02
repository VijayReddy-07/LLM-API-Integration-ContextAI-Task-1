
import logging

import streamlit as st
from chatbot import generate_response_stream

st.set_page_config(
    page_title="ContextAI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 ContextAI")
st.caption("An intelligent multi-turn AI chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Ask me anything...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Context management: retain last 10 messages
    context = st.session_state.messages[-10:]

    with st.chat_message("assistant"):
        try:
            answer = st.write_stream(generate_response_stream(context))
            if not answer:
                raise RuntimeError("Gemini returned an empty response.")
        except Exception:
            logging.exception("Failed to generate a chatbot response")
            st.error(
                "Gemini could not generate a response. Check your API key "
                "and connection, then review the Streamlit terminal for details."
            )
        else:
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

if st.button("Clear Conversation"):
    st.session_state.messages = []
    st.rerun()
