# client/src/components/interview.py
import streamlit as st
from server.model import fetch_question

def interview_flow(count: int = 5):

    q_index = st.session_state.index
    current_q = st.session_state.questions[q_index]

    st.markdown(f"**Assistant:** {current_q}")
    response = st.text_area("Your Response", key=f"response_{q_index}")

    if q_index < count - 1:
        if st.button("Next"):
            st.session_state.answers.append(response)
            st.session_state.questions.append(fetch_question(response))
            st.session_state.index += 1
            st.rerun()
    else:
        if st.button("Submit Interview"):
            st.session_state.answers.append(response)
            st.session_state.stage = "completed"
            st.rerun()
