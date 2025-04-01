import streamlit as st
from datetime import datetime
import random
import time

# ✅ Page config must be the first Streamlit command
st.set_page_config(page_title="FieldFocus Dashboard", layout="centered")

# ---------- App Branding ---------- #
APP_NAME = "FieldFocus"
APP_TAGLINE = "Train. Think. Thrive."

# ---------- Custom Professional Styling ---------- #
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Inter', sans-serif !important;
            background-color: #f2f2f2 !important;
            color: #0d0d0d !important;
            overflow-x: auto;
        }

        .main, .block-container {
            background-color: #f2f2f2 !important;
        }

        .stTabs [data-baseweb="tab"] {
            color: #333;
            background-color: #e0e0e0;
            padding: 0.6rem;
            border-radius: 8px;
            font-weight: 600;
            white-space: nowrap;
            overflow-x: auto;
        }
        .stTabs [aria-selected="true"] {
            color: #000;
            border-bottom: 3px solid #0077ff;
            background-color: #ffffff;
        }

        .stTextInput > div > div > input,
        .stTextArea > div > textarea {
            background-color: #ffffff;
            color: #000000;
            font-family: 'Inter', sans-serif !important;
        }

        .stButton > button {
            background-color: #0077ff;
            color: white;
            border: none;
            padding: 10px 18px;
            border-radius: 12px;
            font-weight: 600;
        }

        .stSlider > div {
            color: #000000;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Simulated Modules ---------- #
def get_wearable_data():
    return {
        "Heart Rate": random.randint(58, 95),
        "Body Temp": round(random.uniform(36.1, 37.3), 1),
        "Steps Today": random.randint(3000, 12000),
        "Readiness Score": random.randint(60, 100),
        "Sleep Duration (hrs)": round(random.uniform(6.5, 9.2), 1)
    }

def get_ai_reply(message):
    if "defend" in message.lower():
        return "Coach: Stay tighter on the second ball and watch your positioning."
    elif "press" in message.lower():
        return "Coach: Initiate the press from the striker and close the midfield passing lanes."
    elif "tired" in message.lower():
        return "Coach: Prioritize rest and hydrate. No shame in adjusting the load."
    elif "recovery" in message.lower():
        return "Coach: Active recovery or ice bath today — avoid overload."
    elif "nutrition" in message.lower():
        return "Coach: Aim for protein + complex carbs post-training."
    else:
        return "Coach: Good question — let's look at footage later."

def get_youtube_suggestion():
    return "https://www.youtube.com/watch?v=1XnBzZsLJXA", "Bellingham's midfield positioning and awareness."

# ---------- Alert Logic ---------- #
def generate_alerts(sleep, hydrate, stretch, nutrition):
    alerts = []
    if sleep < 6:
        alerts.append("⚠️ Low sleep detected. Prioritize rest tonight.")
    if not hydrate:
        alerts.append("⚠️ Hydration goal not met. Drink more water.")
    if not stretch:
        alerts.append("⚠️ Stretching missed. Consider a short mobility session.")
    if nutrition and any(x in nutrition.lower() for x in ["pizza", "chips", "fried"]):
        alerts.append("⚠️ Junk food logged. Try cleaner options tomorrow.")
    return alerts

# ---------- Streamlit Header ---------- #
st.markdown(f"""
    <h1 style='text-align: center; font-size: 3rem; color: #000;'>⚽ {APP_NAME}</h1>
    <p style='text-align: center; font-size: 1.1rem; color: #444;'>{APP_TAGLINE}</p>
    <hr style='margin-top: -10px;'>
""", unsafe_allow_html=True)

# ---------- AI Prompt & Response ---------- #
st.markdown("### 🤖 Ask the Coach (AI-Powered)")
ai_input = st.text_input("Ask a tactical, physical or mental health question:", key="ai_prompt")
if ai_input:
    ai_response = get_ai_reply(ai_input)
    st.success(ai_response)
