import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="Jude's Daily Dashboard", layout="wide")

# ---------- Custom Styling ---------- #
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
        }
        .main, .block-container {
            padding: 1rem 0.5rem;
            background-color: #121212;
        }
        .card {
            background-color: #1e1e1e;
            border-radius: 14px;
            padding: 1.2rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }
        .stButton > button {
            background-color: #007aff;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
        }
        .stProgress > div > div {
            background-color: #34c759;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff;
        }
        .stTextInput > div > input,
        .stSelectbox > div > div,
        .stTextArea textarea {
            background-color: #2c2c2e !important;
            color: white !important;
            border-radius: 10px;
            border: 1px solid #3a3a3c;
        }
        .stMarkdown hr {
            display: none;
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

def get_tactical_tip():
    tips = [
        "Stay compact in midfield and press as a unit.",
        "Watch for overlapping runs on the left wing.",
        "Keep your body open when receiving under pressure.",
        "Switch play quickly to exploit space.",
        "Anticipate second balls and stay alert."
    ]
    return random.choice(tips)

def generate_vest_metrics():
    hr = random.randint(60, 90)
    br = random.randint(12, 18)
    sleep = random.randint(6, 9)
    nervous = hr > 80 and br > 16 and sleep < 7
    return {
        "Daily Vest": {"Hydration": random.randint(70, 100), "Heart Rate": hr, "Body Temp": round(random.uniform(36.5, 37.5), 1)},
        "Night Vest": {"REM Sleep %": random.randint(20, 35), "Sleep Duration": sleep, "Resting HR": random.randint(50, 65)},
        "Relax Vest": {"Stress Level": random.randint(1, 10), "Breathing Rate": br, "Recovery Score": random.randint(60, 100)},
        "Nervous Triggered": nervous
    }

def get_jude_demo_plan():
    return [
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

# ---------- Layout ---------- #
st.title("Jude’s Daily Dashboard")
st.subheader("🗓️ " + datetime.now().strftime("%A, %d %B %Y"))
matchday = st.checkbox("Matchday Mode", value=False)
metrics = generate_vest_metrics()

if matchday:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.info("You're in Matchday Mode. Stay focused — phone use limited to key reminders.")
    st.markdown("</div>", unsafe_allow_html=True)

if metrics.get("Nervous Triggered"):
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.warning("🧠 Nervousness Detected: Breathe. Remember who you are. Message your family or focus on your purpose.")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🧠 Mental Check-In")
    mood = st.selectbox("How are you feeling this morning?", ["Top Form", "Focused", "Tired", "Stressed", "Low"])
    st.success(get_ai_response(mood))
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 💬 Coach Ancelotti Inbox")
    question = st.text_input("Ask a tactical question to the coaching staff:")
    if st.button("Send to Coach"):
        st.success("Message sent. Coach will follow up in training.")
        st.markdown("#### 🎥 Suggested Drill Video")
        st.video("https://www.youtube.com/watch?v=pN6JK0aYg8Y")
        st.caption("Watch how Bellingham adjusts under pressure.")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🦾 Tri-Vest Metrics")
    for vest, data in metrics.items():
        if isinstance(data, dict):
            with st.expander(vest):
                for k, v in data.items():
                    st.write(f"**{k}:** {v}")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📋 Daily Plan")
    for item in get_jude_demo_plan():
        st.write(f"- {item}")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🔁 Daily XP Tracker")
    xp = random.randint(60, 100)
    st.progress(xp / 100)
    st.caption(f"You've earned {xp} XP – you're moving like a champ.")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🌍 Language of the Day")
    st.info(get_language_phrase())
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🎮 Tactical Tip")
    st.info(get_tactical_tip())
    st.markdown("</div>", unsafe_allow_html=True)

st.caption("⚽ Designed for mobile. Built for focus. Inspired by Jude.")
