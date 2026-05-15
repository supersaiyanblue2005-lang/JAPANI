import streamlit as st
from utils.style import apply_custom_style
from components.header import render_header
from utils.i18n import t

st.set_page_config(page_title="About - JAPANI", page_icon="ℹ️", layout="wide")
apply_custom_style()
render_header()

# VI-17 Hero Section
st.markdown(f"""
<div style="text-align: center; padding: 4rem 2rem; background: linear-gradient(135deg, #1E3A8A 0%, #0a192f 100%); border-radius: 16px; color: white; margin-bottom: 3rem;">
    <h1 style="color: white; font-size: 3rem; margin-bottom: 1rem;">{t('about_hero_title')}</h1>
    <p style="font-size: 1.25rem; opacity: 0.9; max-width: 600px; margin: 0 auto;">
        {t('about_hero_sub')}
    </p>
</div>
""", unsafe_allow_html=True)

# VI-18 Our Solution
st.markdown(f"<h2 style='text-align: center; margin-bottom: 2rem;'>{t('our_solution')}</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div style="background-color: white; padding: 2rem; border-radius: 12px; height: 100%; border: 1px solid #E5E7EB; text-align: center;">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">🧠</div>
        <h3 style="color: #1E3A8A;">{t('sol1_title')}</h3>
        <p style="color: #4B5563; text-align: left;">
            {t('sol1_desc')}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background-color: white; padding: 2rem; border-radius: 12px; height: 100%; border: 1px solid #E5E7EB; text-align: center;">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">⛩️</div>
        <h3 style="color: #1E3A8A;">{t('sol2_title')}</h3>
        <p style="color: #4B5563; text-align: left;">
            {t('sol2_desc')}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="background-color: white; padding: 2rem; border-radius: 12px; height: 100%; border: 1px solid #E5E7EB; text-align: center;">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">📈</div>
        <h3 style="color: #1E3A8A;">{t('sol3_title')}</h3>
        <p style="color: #4B5563; text-align: left;">
            {t('sol3_desc')}
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# VI-19 CTA
st.markdown(f"""
<div style="text-align: center; padding: 3rem; background-color: #E0F2FE; border-radius: 16px;">
    <h2 style="color: #0a192f; margin-bottom: 1.5rem;">{t('ready')}</h2>
</div>
""", unsafe_allow_html=True)

_, col_center, _ = st.columns([1, 1, 1])
with col_center:
    if st.button(t('get_started'), type="primary", use_container_width=True):
        st.switch_page("app.py")
