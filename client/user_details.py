# client/src/components/user_details.py
import streamlit as st
from server.model import fetch_question

def user_info():
    with st.form("candidate_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.number_input("Years of Experience", min_value=0.0, step=0.5)
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (Languages, Frameworks, Tools, etc.)")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.session_state.candidate_info = {
                "Full Name": full_name,
                "Email": email,
                "Phone": phone,
                "Experience": experience,
                "Position": position,
                "Location": location,
                "Tech Stack": tech_stack,
            }

             # Generate questions here before proceeding
            st.session_state.questions.append(fetch_question(tech_stack))
            st.session_state.chat_history.append(("bot", "Thank you! Let's begin the interview."))
            st.session_state.stage = "interview"
