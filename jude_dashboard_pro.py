import streamlit as st
from datetime import datetime
import random
import time

# ✅ Page config must be the first Streamlit command
st.set_page_config(page_title="FieldFocus Dashboard", layout="centered")

# ---------- App Branding ---------- #
APP_NAME = "FieldFocus"
APP_TAGLINE = "Train. Think. Thrive."

# ---------- Custom Dark Styling ---------- #
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Inter', sans-serif !important;
            background-color: #0e0e0e !important;
            color: #f0f0f0 !important;
            overflow-x: hidden;
        }

        .main, .block-container {
            background-color: #0e0e0e !important;
        }

        .stTabs > div {
            overflow-x: auto !important;
            white-space: nowrap !important;
            display: flex;
            align-items: center;
            margin-bottom: -20px; /* Reduce space under the tabs */
            padding-bottom: 10px; /* Adjust padding for visual balance */
        }

        .stTabs [data-baseweb="tab"] {
            color: #ccc;
            background-color: #1a1a1a;
            padding: 0.6rem;
            border-radius: 8px;
            font-weight: 600;
            display: inline-block;
            margin-right: 10px;
        }

        .stTabs [aria-selected="true"] {
            color: #fff;
            border-bottom: 3px solid #00bfff;
            background-color: #1f1f1f;
        }

        .stTextInput > div > div > input,
        .stTextArea > div > textarea {
            background-color: #1f1f1f;
            color: #ffffff;
            font-family: 'Inter', sans-serif !important;
        }

        .stButton > button {
            background-color: #00bfff;
            color: white;
            border: none;
            padding: 10px 18px;
            border-radius: 12px;
            font-weight: 600;
        }

        .stSlider > div {
            color: #ffffff;
        }

        /* Scrollbars customization */
        ::-webkit-scrollbar {
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #1a1a1a;
        }
        ::-webkit-scrollbar-thumb {
            background-color: #00bfff;
            border-radius: 10px;
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

# ---------- Tab Layout ---------- #
tabs = st.tabs([
    "Daily Info", "Routine", "Tactics", "Nutrition", "Calendar", "Mental Prep", "Emotion Check", "Recovery"
])

with tabs[0]:
    st.subheader("📅 Daily Schedule")
    schedule_input = st.text_area("What does your day look like today?")
    st.subheader("🩺 Wearable Check-In")
    data = get_wearable_data()
    for k, v in data.items():
        st.write(f"**{k}:** {v}")

with tabs[1]:
    st.subheader("📋 Daily Routine")
    st.markdown("""
    - Wake up 7:30AM, hydration + mobility
    - Breakfast: eggs, avocado toast, smoothie
    - Team training 10AM - 12PM
    - Lunch + Recovery Nap
    - Gym: Mobility & core work
    - Film review session (30 mins)
    - Dinner: lean protein + complex carbs
    - Spanish practice (Duolingo or app)
    - 10 mins meditation + Sleep by 10:30PM
    """)

with tabs[2]:
    st.subheader("🎮 Tactical Insight")
    st.info("Keep your body open when receiving under pressure.")
    link, cap = get_youtube_suggestion()
    st.video(link)
    st.caption(cap)
    st.text_area("🧠 Player Notes", "")
    st.text_area("📣 Notes for Staff", "")

with tabs[3]:
    st.subheader("🍽️ Smart Nutrition Tracker")
    meal = st.text_input("What did you eat today?")
    if meal:
        if any(x in meal.lower() for x in ["chips", "pizza", "fried"]):
            st.warning("⚠️ High-fat foods detected — try switching to grilled options.")
        elif any(x in meal.lower() for x in ["chicken", "eggs", "smoothie", "salad"]):
            st.success("✅ Great choice! Balanced nutrition fuels top performance.")
        else:
            st.info("🍴 Nutrition logged.")

with tabs[4]:
    st.subheader("🗓️ Weekly Calendar")
    st.text_input("Monday", "Training")
    st.text_input("Tuesday", "Gym + Recovery")
    st.text_input("Wednesday", "Tactical Drills")

with tabs[5]:
    st.subheader("🧘 Guided Mental Preparation")
    focus_type = st.selectbox("Pick your focus today:", ["Visualization", "Breathing", "Gratitude"])
    if focus_type == "Visualization":
        st.info("Picture your perfect pass, tackle, or goal.")
    elif focus_type == "Breathing":
        st.info("Try box breathing: inhale 4s, hold 4s, exhale 4s, hold 4s. Repeat 4x.")
    else:
        st.info("Think of 3 things you’re grateful for.")

with tabs[6]:
    st.subheader("😌 Emotional Check-In")
    mood = st.radio("How are you feeling?", ["🔥 On fire", "🙂 Focused", "😴 Tired", "😟 Nervous", "😢 Low"])
    if mood == "😟 Nervous":
        st.info("Reach out to family or teammates for support.")
    elif mood == "😢 Low":
        st.warning("It's okay to not feel 100%. Reflect, rest, and reset.")
    elif mood == "😴 Tired":
        st.warning("Energy seems low. Hydrate and rest early.")
    else:
        st.success("You're in a good headspace. Keep it up!")

with tabs[7]:
    st.subheader("🛌 Recovery Tracker")
    hours_slept = st.slider("How many hours did you sleep?", 0, 12, 8)
    did_stretch = st.checkbox("Did you stretch today?")
    did_hydrate = st.checkbox("Have you drunk 2L+ of water?")
    alerts = generate_alerts(hours_slept, did_hydrate, did_stretch, meal if 'meal' in locals() else "")
    for a in alerts:
        st.warning(a)
    if not alerts:
        st.success("✅ You’re recovering like a pro. Stay consistent!")
