import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="Jude's Daily Dashboard", layout="wide")

# ---------- Styling ---------- #
st.markdown("""
    <style>
        body {
            background-color: #f0f0f0;
            color: #000000;
        }
        .main, .block-container {
            background-color: #f0f0f0 !important;
            padding: 2rem 1rem;
        }
        .card {
            background-color: #ffffff;
            border-radius: 20px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .stButton > button {
            background-color: #111;
            color: white;
            border-radius: 10px;
            padding: 8px 14px;
            font-size: 15px;
            font-weight: 600;
        }
        .stProgress > div > div {
            background-color: #007aff;
            border-radius: 10px;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #111;
        }
        .stExpanderHeader {
            font-size: 16px;
            font-weight: 500;
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

def get_jude_demo_plan():
    return [
        "Wake up 7:30AM, hydration + light mobility",
        "Breakfast: eggs, avocado toast, smoothie",
        "Team training 10AM - 12PM",
        "Lunch + Recovery Nap",
        "Gym: Mobility & core (optional)",
        "Film review session (30 mins)",
        "Dinner: lean protein + complex carbs",
        "Light Spanish practice (Duolingo or app)",
        "Meditation 10 mins + Sleep by 10:30PM"
    ]

# ---------- Main Content ---------- #
st.title("Jude’s Daily Dashboard")
st.subheader("🗓️ " + datetime.now().strftime("%A, %d %B %Y"))

# Mental Check-In
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🧠 Mental Check-In")
    mood = st.selectbox("How are you feeling this morning?", ["Top Form", "Focused", "Tired", "Stressed", "Low"])
    st.info(get_ai_response(mood))
    st.markdown("</div>", unsafe_allow_html=True)

# Recovery Status
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 💪 Recovery Status")
    recovery_score = random.randint(60, 100)
    st.progress(recovery_score / 100)
    if recovery_score > 85:
        st.success("You’re fresh. Green light for full intensity today.")
    elif recovery_score > 70:
        st.warning("You're in decent shape, but stay hydrated and monitor fatigue.")
    else:
        st.error("Recovery’s not optimal. Focus on mobility, sleep, and hydration today.")
    st.markdown("</div>", unsafe_allow_html=True)

# Daily Gameplan
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
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
    st.markdown("</div>", unsafe_allow_html=True)

# Jude's Real Day Demo
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📋 Jude’s Proven Daily Flow")
    for task in get_jude_demo_plan():
        st.markdown(f"- {task}")
    st.markdown("</div>", unsafe_allow_html=True)

# XP Progress
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📈 Daily XP Progress")
    xp = random.randint(25, 90)
    st.progress(xp / 100)
    st.caption(f"You've earned {xp} XP today – nice!")
    st.markdown("</div>", unsafe_allow_html=True)

# Connect & Recharge Placeholder
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🤝 Connect & Recharge (Coming Soon)")
    st.markdown("Send a quick message to a teammate or post a motivational quote for your fans.")
    st.markdown("AI will soon suggest ways to connect when your mood or recovery drops.")
    st.markdown("When you're ready, we can add actual messaging tools, fan interaction mockups, or even tie-ins with WhatsApp/Instagram APIs (if taken pro level).")
    st.markdown("</div>", unsafe_allow_html=True)

# Quick Reflection
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📓 Quick Reflection")
    journal = st.text_area("Write anything on your mind (optional)", "")
    if journal:
        st.success("Reflection saved. Mental sharpness unlocked.")
    st.markdown("</div>", unsafe_allow_html=True)

# Tactical Coach
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🎮 Tactical Coach Tip")
    st.info(get_tactical_tip())
    st.markdown("---")
    st.markdown("**Ask Coach Ancelotti or Real Madrid Analyst (Coming Soon)**")
    st.text_input("Ask a tactical question to the coaching staff or analytics team")
    st.button("Send Question")
    st.markdown("</div>", unsafe_allow_html=True)

# Language Learning
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🌍 Language of the Day")
    st.success(get_language_phrase())
    st.markdown("</div>", unsafe_allow_html=True)

# Tri-Vest Metrics
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🦾 Tri-Vest Body Metrics")
    metrics = generate_vest_metrics()
    for vest, data in metrics.items():
        with st.expander(f"{vest}"):
            for key, value in data.items():
                st.write(f"**{key}:** {value}")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Designed for mobile. Inspired by Jude. ⚽")
st.caption("© 2023 Jude's Dashboard. All rights reserved.")
st.markdown("Made with ❤️ by Jude Bellingham & AI Team")