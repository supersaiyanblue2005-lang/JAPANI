import streamlit as st

def apply_custom_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Noto+Sans+JP:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', 'Noto Sans JP', sans-serif;
        background-color: #F9FAFB;
        color: #0a192f;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #0a192f;
        font-family: 'Inter', 'Noto Sans JP', sans-serif;
        font-weight: 600;
    }

    /* Primary Buttons */
    .stButton > button {
        background-color: #1E3A8A;
        color: #FFFFFF;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #1e40af;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        color: #FFFFFF;
    }

    /* Cards / Containers */
    div[data-testid="stVerticalBlock"] > div[style*="border"] {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        border: 1px solid #E5E7EB;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E5E7EB;
    }
    
    /* Text Area */
    .stTextArea textarea {
        border-radius: 8px;
        border: 1px solid #E5E7EB;
        padding: 1rem;
    }
    
    /* Radio and Selectbox */
    .stRadio > div, .stSelectbox > div > div {
        background-color: transparent;
    }

    /* Progress bar */
    .stProgress > div > div > div > div {
        background-color: #1E3A8A;
    }
    
    /* Tags / Pills style */
    .suggestion-box {
        background-color: #E0F2FE;
        border: 1px solid #BAE6FD;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 0.5rem;
        color: #0a192f;
    }
    </style>
    """, unsafe_allow_html=True)
