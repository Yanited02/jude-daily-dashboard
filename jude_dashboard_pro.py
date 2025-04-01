import streamlit as st
from datetime import datetime
import random
import time

# ---------- Simulated Modules ---------- #
def get_wearable_data():
    return {
        "Heart Rate": random.randint(58, 95),
        "Body Temp": round(random.uniform(36.1, 37.3), 1),
        "Steps Today": random.randint(3000, 12000),
        "Readiness Score": random.randint(60, 100),
        "Sleep Duration (hrs)": round(random.uniform(6.5, 9.2), 1)
    }

chat_log = []

def send_message(user, msg):
    chat_log.append((datetime.now().strftime("%H:%M"), user, msg))
    return True

def get_chat_history():
    return chat_log[-5:]

# ---------- UI Styling ---------- #
st.markdown("""
    <style>
        body { background-color: #121212; color: #ffffff; }
        .main, .block-container { padding: 1rem 0.5rem; background-color: #121212; }
        .card { background-color: #1e1e1e; border-radius: 14px; padding: 1.2rem; margin-bottom: 1rem; box-shadow: 0 2px 6px rgba(0,0,0,0.2); }
        .stButton > button { background-color: #007aff; color: white; border-radius: 10px; padding: 10px 20px; font-size: 16px; border: none; }
        .stProgress > div > div { background-color: #34c759; }
        h1, h2, h3, h4, h5, h6 { color: #ffffff; }
        .stTextInput > div > input, .stSelectbox > div > div, .stTextArea textarea {
            background-color: #2c2c2e !important;
            color: white !important;
            border-radius: 10px;
            border: 1px solid #3a3a3c;
        }
        .stMarkdown hr { display: none; }
    </style>
""", unsafe_allow_html=True)

# ---------- Intro Splash ---------- #
st.markdown("<h1 style='text-align: center; font-size: 40px;'>👟 PulsePoint</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Where performance meets lifestyle</p>", unsafe_allow_html=True)
with st.spinner("Warming up..."):
    time.sleep(2.5)

# ---------- Main Dashboard ---------- #
st.title("Jude’s Daily Dashboard")
st.subheader("🗓️ " + datetime.now().strftime("%A, %d %B %Y"))
matchday = st.checkbox("Matchday Mode", value=False)
vest_metrics = {
    "Daily Vest": {"Hydration": random.randint(70, 100), "Heart Rate": random.randint(60, 90), "Body Temp": round(random.uniform(36.5, 37.5), 1)},
    "Night Vest": {"REM Sleep %": random.randint(20, 35), "Sleep Duration": random.randint(6, 9), "Resting HR": random.randint(50, 65)},
    "Relax Vest": {"Stress Level": random.randint(1, 10), "Breathing Rate": random.randint(12, 18), "Recovery Score": random.randint(60, 100)}
}

if matchday:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.info("You're in Matchday Mode. Stay focused — phone use limited to key reminders.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Sections ---------- #
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🔗 Wearable Fitness Insights")
    for key, val in get_wearable_data().items():
        st.write(f"**{key}:** {val}")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🦾 Tri-Vest Metrics")
    for vest, data in vest_metrics.items():
        with st.expander(vest):
            for k, v in data.items():
                st.write(f"**{k}:** {v}")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📋 Daily Routine")
    routine = [
        "Wake up 7:30AM, hydration + mobility",
        "Breakfast: eggs, avocado toast, smoothie",
        "Team training 10AM - 12PM",
        "Lunch + Recovery Nap",
        "Gym: Mobility & core work",
        "Film review session (30 mins)",
        "Dinner: lean protein + complex carbs",
        "Spanish practice (Duolingo or app)",
        "10 mins meditation + Sleep by 10:30PM"
    ]
    for item in routine:
        st.write(f"- {item}")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 💬 Pulse Chat")
    user_input = st.text_input("Message Coach or AI Assistant:")
    if st.button("Send"):
        send_message("Jude", user_input)
    for timestamp, user, msg in get_chat_history():
        st.markdown(f"`{timestamp}` **{user}**: {msg}")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🎮 Tactical Tip")
    st.info(random.choice([
        "Stay compact in midfield and press as a unit.",
        "Watch for overlapping runs on the left wing.",
        "Keep your body open when receiving under pressure.",
        "Switch play quickly to exploit space.",
        "Anticipate second balls and stay alert."
    ]))
    st.markdown("</div>", unsafe_allow_html=True)

st.caption("⚽ PulsePoint – Elite lifestyle tracking inspired by Jude.")
