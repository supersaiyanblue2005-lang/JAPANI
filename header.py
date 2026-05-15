import streamlit as st

def render_header():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.markdown("<h2 style='margin: 0; padding: 0;'>💬 JAPANI</h2>", unsafe_allow_html=True)
    with col3:
        # Language Switcher
        st.radio(
            "Language",
            ["EN", "JP", "VI"],
            horizontal=True,
            label_visibility="collapsed",
            key="lang_switcher"
        )
    st.markdown("<hr style='margin-top: 0.5rem; margin-bottom: 2rem;'/>", unsafe_allow_html=True)
