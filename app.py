import streamlit as st

APP_NAME = "FieldFocus"
APP_TAGLINE = "Train. Think. Thrive."

st.set_page_config(page_title=f"{APP_NAME} Dashboard", layout="centered")
st.markdown(f"""
<h1 style='text-align: center; font-size: 3rem;'>⚽ {APP_NAME}</h1>
<p style='text-align: center; font-size: 1.1rem; color: gray;'>{APP_TAGLINE}</p>
<hr style='margin-top: -10px;'>
""", unsafe_allow_html=True)

st.success("✅ FieldFocus is installed and running! Add your full tab logic below.")
