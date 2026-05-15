import streamlit as st
import datetime
from utils.style import apply_custom_style
from components.header import render_header
from utils.ai import analyze_japanese_text
from utils.i18n import t

st.set_page_config(
    page_title="JAPANI - AI Japanese Assistant",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply CSS
apply_custom_style()

# Header
render_header()

# Sidebar / Left Side (VI-01 to VI-04)
with st.sidebar:
    st.markdown(f"### {t('culture_context')}")
    
    culture = st.selectbox(
        t("culture_label"),
        [t("culture_workplace"), t("culture_daily"), t("culture_event")],
        index=0
    )
    
    relationship = st.selectbox(
        t("relationship_label"),
        [t("rel_boss"), t("rel_colleague"), t("rel_client"), t("rel_friend")]
    )
    
    st.markdown(f"### {t('purpose_title')}")
    purpose = st.radio(
        t("purpose_label"),
        [
            t("purp_convey"),
            t("purp_opinion"),
            t("purp_request"),
            t("purp_thanks"),
            t("purp_apologize"),
            t("purp_decline")
        ]
    )
    
    st.divider()
    
    # 1 Day 1 Fact Widget (VI-04)
    st.markdown(f"### {t('fact_title')}")
    st.info(t("fact_content"))

# Main Content (VI-05 to VI-11)
st.markdown(f"### {t('msg_analysis')}")

input_text = st.text_area(
    t("input_label"),
    height=150,
    placeholder=t("input_placeholder"),
    max_chars=1000
)

if st.button(t("analyze_btn"), type="primary"):
    if not input_text:
        st.error(t("error_empty"))
    else:
        with st.spinner(t("analyzing")):
            results = analyze_japanese_text(input_text, culture, relationship, purpose)
            
            st.success(t("analysis_complete"))
            
            # Results UI
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(t("formality"), f"{results['formality']}%")
                st.progress(results['formality'] / 100)
            with col2:
                st.metric(t("naturalness"), f"{results['naturalness']}%")
                st.progress(results['naturalness'] / 100)
            with col3:
                # We also translate the relevance string if needed
                rel_label = t(results['relevance'].lower()) if results['relevance'].lower() in ['high', 'medium', 'low'] else results['relevance']
                st.metric(t("relevance"), rel_label)
                # Mock a progress bar for relevance
                rel_score = 1.0 if results['relevance'] == "High" else (0.5 if results['relevance'] == "Medium" else 0.2)
                st.progress(rel_score)
            
            st.markdown("---")
            
            st.markdown(f"#### {t('overall')}")
            st.write(results['overall'])
            
            st.markdown(f"#### {t('culture_exp')}")
            st.info(results['culture_explanation'])
            
            st.markdown(f"#### {t('rewrite_sugg')}")
            for suggestion in results['rewrite_suggestions']:
                st.markdown(f'<div class="suggestion-box">{suggestion}</div>', unsafe_allow_html=True)
                
            st.markdown(f"#### {t('related_expr')}")
            for expr in results['related_expressions']:
                st.markdown(f"- {expr}")
