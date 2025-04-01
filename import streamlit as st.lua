import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="Jude's Daily Dashboard", layout="centered")

# ---------- Styling ---------- #
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stButton > button {
            background-color: #111;
            color: white;
            border-radius: 12px;
            padding: 10px 16px;
            font-size: 16px;
        }
        .stProgress > div > div {
            background-color: #2d2d2d;
        }
        .stSlider > div {
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Helper Functions ---------- #
def get_ai_response(mood):
    responses = {
        "Top Form": "Love that energy, Jude. Let’s dominate today.",
        "Focused": "Dialed in. Madrid mode activated.",
        "Tired": "Alright, we’ll ease into the day. Recovery is key.",
        "Stressed": "Let’s take a breath. One touch at a time.",
        "Low": "Let’s reset. You’re still a baller even on off days."
    }
    return responses.get(mood, "Ready when you are.")

def get_tactical_tip():
    tips = [
        "Stay compact in midfield and press as a unit.",
        "Watch for overlapping runs on the left wing.",
        "Keep your body open when receiving under pressure.",
        "Switch play quickly to exploit space.",
        "Anticipate second balls and stay alert."
    ]
    return random.choice(tips)

def get_language_phrase():
    phrases = {
        "Vamos": "Let's go (Spanish)",
        "Buen pase": "Good pass (Spanish)",
        "Golazo": "Amazing goal (Spanish)",
        "Pressing alto": "High pressing (Spanish)",
        "Cambio": "Substitution (Spanish)"
    }
    phrase, meaning = random.choice(list(phrases.items()))
    return f"**{phrase}** – {meaning}"

def generate_vest_metrics():
    return {
        "Daily Vest": {
            "Hydration": random.randint(70, 100),
            "Heart Rate": random.randint(60, 90),
            "Body Temp": round(random.uniform(36.5, 37.5), 1)
        },
        "Night Vest": {
            "REM Sleep %": random.randint(20, 35),
            "Sleep Duration": random.randint(6, 9),
            "Resting HR": random.randint(50, 65)
        },
        "Relax Vest": {
            "Stress Level": random.randint(1, 10),
            "Breathing Rate": random.randint(12, 18),
            "Recovery Score": random.randint(60, 100)
        }
    }

# ---------- Main Content ---------- #
st.title("Jude’s Daily Dashboard")
st.subheader(datetime.now().strftime("📅 %A, %d %B %Y"))

# Mood Tracker
st.markdown("### 🧠 Mental Check-In")
mood = st.selectbox("How are you feeling this morning?", ["Top Form", "Focused", "Tired", "Stressed", "Low"])
st.info(get_ai_response(mood))

# Recovery Meter
st.markdown("### 💪 Recovery Status")
recovery_score = random.randint(60, 100)
st.progress(recovery_score / 100)
if recovery_score > 85:
    st.success("You’re fresh. Green light for full intensity today.")
elif recovery_score > 70:
    st.warning("You're in decent shape, but stay hydrated and monitor fatigue.")
else:
    st.error("Recovery’s not optimal. Focus on mobility, sleep, and hydration today.")

# Daily Plan
st.markdown("### 🎯 Daily Gameplan")
col1, col2 = st.columns(2)
with col1:
    st.write("📌 Breakfast: Protein oats + fruit")
    st.write("🏋️ Gym: Upper body strength")
    st.write("🧘‍♂️ Recovery: Yoga 20 mins")
with col2:
    st.write("🥗 Lunch: Grilled chicken + quinoa")
    st.write("🎮 Break: 45 mins FIFA")
    st.write("🛏 Sleep Target: 9 hours")

# XP Bar
st.markdown("### 📈 Daily XP Progress")
xp = random.randint(25, 90)
st.progress(xp / 100)
st.caption(f"You've earned {xp} XP today – nice!")

# Journal (Optional)
st.markdown("### 📓 Quick Reflection")
journal = st.text_area("Write anything on your mind (optional)", "")
if journal:
    st.success("Reflection saved. Mental sharpness unlocked.")

# Tactical Coach
st.markdown("### 🎮 Tactical Coach Tip")
st.info(get_tactical_tip())

# Language Learning
st.markdown("### 🌍 Language of the Day")
st.success(get_language_phrase())

# Tri-Vest Metrics
st.markdown("### 🦾 Tri-Vest Body Metrics")
metrics = generate_vest_metrics()
for vest, data in metrics.items():
    with st.expander(f"{vest}"):
        for key, value in data.items():
            st.write(f"**{key}:** {value}")

# Footer
st.markdown("---")
st.caption("Designed for mobile. Inspired by Jude. ⚽")