# client/src/components/chat.py
import streamlit as st

def display_chat():
    for speaker, msg in st.session_state.chat_history:
        if speaker == "bot":
            st.markdown(f"**Assistant:** {msg}")
        else:
            st.markdown(f"**You:** {msg}")
