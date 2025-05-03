# client/src/components/summary.py
import streamlit as st

def show_summary():
    st.success("🎉 Interview Completed! Thank you.")
    st.markdown("### Candidate Info:")
    for k, v in st.session_state.candidate_info.items():
        st.markdown(f"- **{k}**: {v}")

    st.markdown("### Interview Responses:")
    for i, q in enumerate(st.session_state.questions):
        st.markdown(f"**Q{i+1}: {q}**")
        st.markdown(f"- **Answer**: {st.session_state.answers[i]}")
