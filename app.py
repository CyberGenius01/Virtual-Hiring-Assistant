# client/src/app.py
import streamlit as st
from client import greet_user, user_info, show_summary, display_chat, interview_flow

# Initialize session state
if "stage" not in st.session_state:
    st.session_state.stage = "intro"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {}
if "index" not in st.session_state:
    st.session_state.index = 0
if "questions" not in st.session_state:
    st.session_state.questions = []
if "answers" not in st.session_state:
    st.session_state.answers = []

# --- Streamlit App ---
st.title("Vitrual Hiring Assistant")

if st.session_state.stage == "intro":
    if not st.session_state.chat_history:
        st.session_state.chat_history.append(("bot", greet_user()))
    display_chat()
    user_info()

elif st.session_state.stage == "interview":
    # Show previous Q&A
    if st.session_state.answers:
        for i in range(len(st.session_state.questions) - 1):
            st.markdown(f"**Assistant Q{i+1}: {st.session_state.questions[i]}**")
            st.markdown(
                f"<div style='text-align: right; color: #1f77b4;'><strong>🧑 You:</strong> {st.session_state.answers[i]}</div>",
                unsafe_allow_html=True
            )
    interview_flow()

elif st.session_state.stage == "completed":
    show_summary()
