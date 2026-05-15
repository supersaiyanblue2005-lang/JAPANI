import streamlit as st
from utils.style import apply_custom_style
from components.header import render_header
from utils.i18n import t

# Set page config
st.set_page_config(page_title="Search History - JAPANI", page_icon="🕒", layout="wide")
apply_custom_style()
render_header()

st.markdown(f"## {t('history_title')}")

# Filters (VI-12, VI-13, VI-14)
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    search_query = st.text_input(t('search_kw'), max_chars=100)
with col2:
    context_filter = st.selectbox(
        t('filter_context'),
        [t('all_contexts'), t('rel_boss'), t('rel_colleague'), t('rel_client'), t('rel_friend')]
    )
with col3:
    sort_by = st.selectbox(t('sort_date'), [t('sort_new'), t('sort_old')])

st.markdown("---")

# Mock History Data
history_data = [
    {
        "id": 1,
        "date": "2024-05-15 10:30",
        "original": "明日時間ありますか？相談したいことあります。",
        "context": t("rel_boss"),
        "formality": 40,
        "naturalness": 70
    },
    {
        "id": 2,
        "date": "2024-05-14 15:20",
        "original": "資料を確認してください。",
        "context": t("rel_client"),
        "formality": 50,
        "naturalness": 60
    },
    {
        "id": 3,
        "date": "2024-05-10 09:15",
        "original": "お疲れ様です。昨日の件ですが...",
        "context": t("rel_colleague"),
        "formality": 85,
        "naturalness": 90
    }
]

# Display Cards (VI-15, VI-16)
for item in history_data:
    # Filter logic (basic mock)
    if context_filter != t('all_contexts') and item["context"] != context_filter:
        continue
    if search_query and search_query not in item["original"]:
        continue
        
    with st.container():
        st.markdown(f"""
        <div style="background-color: white; padding: 1.5rem; border-radius: 12px; border: 1px solid #E5E7EB; margin-bottom: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <span style="color: #6B7280; font-size: 0.875rem;">{item['date']}</span>
                    <h4 style="margin-top: 0.5rem; color: #0a192f;">{item['original']}</h4>
                    <span style="background-color: #E0F2FE; color: #1E3A8A; padding: 0.25rem 0.75rem; border-radius: 999px; font-size: 0.875rem; font-weight: 600;">{item['context']}</span>
                    <div style="margin-top: 1rem; font-size: 0.875rem; color: #4B5563;">
                        {t('formality')}: <b>{item['formality']}%</b> &nbsp;|&nbsp; {t('naturalness')}: <b>{item['naturalness']}%</b>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Actions
        col_act1, col_act2, col_space = st.columns([1, 1, 8])
        with col_act1:
            if st.button(t('view_detail'), key=f"view_{item['id']}", use_container_width=True):
                st.info("Redirecting to detail view...")
        with col_act2:
            if st.button(t('delete'), key=f"del_{item['id']}", use_container_width=True):
                st.warning(t('deleted'))
